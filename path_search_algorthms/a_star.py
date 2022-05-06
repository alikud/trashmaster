from data_structures.heap import Heap
from path_search_algorthms import a_star_utils as utils

def search_path(start_x: int, start_y: int, agent_rotation: utils.Rotation, target_x: int, target_y: int, array):

    start_node = utils.Node(start_x, start_y, agent_rotation)
    target_node = utils.Node(target_x, target_y, utils.Rotation.NONE)

    # heap version

    # nodes for check
    search_list = Heap()
    search_list.append(start_node, 0)

    # checked nodes
    searched_list: list[(int, int)] = []

    while (search_list.length() > 0):
        node: utils.Node = search_list.take_first()

        searched_list.append((node.x, node.y))

        # check for target node
        if ((node.x, node.y) == (target_x, target_y)):
            return trace_path(node)

        # neightbours processing
        neighbours = utils.get_neighbours(node, searched_list, array)
        for neighbour in neighbours:

            # calculate new g cost for neightbour (start -> node -> neightbour)
            new_neighbour_cost = node.g_cost + utils.get_neighbour_cost(node, neighbour)

            if (new_neighbour_cost < neighbour.g_cost or not search_list.contains(neighbour)):

                # replace cost and set parent node
                neighbour.g_cost = new_neighbour_cost
                neighbour.h_cost = utils.get_h_cost(neighbour, target_node)
                neighbour.parent = node

                # add to search 
                if(not search_list.contains(neighbour)):
                    search_list.append(neighbour, neighbour.f_cost())

    # array version

    # nodes for check
    # search_list = [start_node]

    # checked nodes
    # searched_list: list[(int, int)] = []

    # while (len(search_list) > 0):
    #     node = search_list[0]

    #     # find cheapest node in search_list
    #     for i in range(1, len(search_list)):
    #         if (search_list[i].f_cost() <= node.f_cost()):
    #             if(search_list[i].h_cost < node.h_cost):
    #                 node = search_list[i]

    #     search_list.remove(node)
    #     searched_list.append((node.x, node.y))

    #     # check for target node
    #     if ((node.x, node.y) == (target_x, target_y)):
    #         return trace_path(node)

    #     # neightbours processing
    #     neighbours = utils.get_neighbours(node, searched_list, array)
    #     for neighbour in neighbours:

    #         # calculate new g cost for neightbour (start -> node -> neightbour)
    #         new_neighbour_cost = node.g_cost + utils.get_neighbour_cost(node, neighbour)

    #         if (new_neighbour_cost < neighbour.g_cost or neighbour not in search_list):

    #             # replace cost and set parent node
    #             neighbour.g_cost = new_neighbour_cost
    #             neighbour.h_cost = utils.get_h_cost(neighbour, target_node)
    #             neighbour.parent = node

    #             # add to search 
    #             if(neighbour not in search_list):
    #                 search_list.append(neighbour)

def trace_path(end_node: utils.Node):
    path = []
    node = end_node

    # set final rotation of end_node because we don't do it before
    node.rotation = utils.get_needed_rotation(node.parent, node)

    while (node.parent != 0):
        move = utils.get_move(node.parent, node)
        path += move
        node = node.parent

    # delete move on initial tile
    path.pop()

    # we found path from end, so we need to reverse it (get_move reverse move words)
    path.reverse()

    # last forward to destination
    path.append("forward")

    return path



        