# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from data_structures.graphs.graphs import Graph

DEBUG = True if __name__ == '__main__' else False


class SceneGraphWorld:
    """Represents the entire rendering domain, encapsulating multiple
    scene graphs (which could be thought as a group of connected components
    in graph theory terminology)."""

    def __init__(self, scene_data=None):
        self.objects = {}
        if scene_data is not None:
            for name, val in scene_data.iteritems():
                self.__setitem__(name, val)

    def __setitem__(self, name, item_objects):
        self.objects[name] = item_objects

    def __delitem__(self, name):
        del self.objects[name]

    def __str__(self):
        for name, scene_graph in self.objects.iteritems():
            print('Total sub-objects in `{}` object = {}:'.format(
                name, scene_graph.total_objects))
            scene_graph.render()

    def render(self):
        self.__str__()


class SceneGraph(Graph):
    """Represents a graph of various objects that is meant to conceptually
    comprise a single entity, even though there may be multiple 3-d
    meshes/polygons, etc inside of it."""

    def __init__(self):
        super(SceneGraph, self).__init__(vertices={})
        self.total_objects = 0

    def __str__(self):
        display = []
        for vertex, vertices in self.vertices.iteritems():
            pos = 'x: {}, y: {}, z: {}'.format(*vertices['pos'])
            display.append('  ["{name}"] -> {val} @ [{pos}]'.format(
                name=vertex, val=vertices['val'], pos=pos))
        return ',\n'.join(display)

    def __delitem__(self, *args, **kwargs):
        super(SceneGraph, self).__delitem__(*args, **kwargs)
        self.total_objects -= 1

    def add_object(self, object_name, mesh_data, position=(0, 0, 0)):
        """Just using `mesh_data` as a generic term. It would probably
        be more prudent to call it `data`, since it can be a mesh, polygon, or
        some other type of 3d-representation."""
        self.total_objects += 1
        super(SceneGraph, self).__setitem__(object_name, {
            'edges': [self.total_objects], 'pos': position, 'val': mesh_data})

    def render(self):
        print(self.__str__())


class DocumentArtboard(Graph):
    """A Photoshop/Illustrator-esque "document" class, where layers can
    be stored as a graph. The connections are not terribly useful, since it's
    effectively a stack, but it can still be used, especially if there are
    nested pieces that make up a single arbitrary 'shape', such as multiple
    <path> elements."""

    def __init__(self, *args, **kwargs):
        super(DocumentArtboard, self).__init__(*args, **kwargs)
        self.current_layer = 0

    def __delitem__(self, *args, **kwargs):
        super(DocumentArtboard, self).__delitem__(*args, **kwargs)
        self.current_layer -= 1

    def __str__(self):
        display = []
        count = 0
        for vertex, vertices in self.vertices.iteritems():
            display.append('[Layer {vertex} "{name}" ({type})] -> {val}'.format(
                ' ' * count, vertex=count, type=vertices['type'],
                name=vertex, val=vertices['val']))
            count += 1
        return ',\n'.join(display)

    def add_layer(self, layer_name, data, shape='path'):
        self.current_layer += 1
        self.__setitem__(
            layer_name,
            {'edges': [self.current_layer], 'type': shape, 'val': data})

    def render(self):
        print(self.__str__())

if DEBUG:
    with Section('Scene graph - 3d renderer'):
        world = SceneGraphWorld()
        rider = SceneGraph()
        rider.add_object(
            'horse', mesh_data='<mesh_data>', position=(100, 200, 15))
        rider.add_object(
            'knight', mesh_data='<mesh_data>', position=(100, 220, 20))
        world['rider'] = rider
        world.render()

    with Section('Scene graph - artboard document'):
        my_illustration = DocumentArtboard()
        my_illustration.add_layer('Face', '<svg_data>', shape='ellipse')
        my_illustration.add_layer('Hair', '<svg_data>', shape='ellipse')
        my_illustration.add_layer('Eye_left', '<svg_data>', shape='ellipse')
        my_illustration.add_layer('Eye_right', '<svg_data>', shape='ellipse')
        my_illustration.add_layer('Mouth', '<svg_data>', shape='path')
        my_illustration.add_layer('Mustache', '<svg_data>', shape='path')
        my_illustration.add_layer('Nose', '<svg_data>', shape='triangle')
        my_illustration.render()
