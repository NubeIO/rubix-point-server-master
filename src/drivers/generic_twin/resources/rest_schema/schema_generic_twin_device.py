from copy import deepcopy

from flask_restful import fields

from src.drivers.generic_twin.resources.rest_schema.schema_generic_twin_point import generic_twin_point_all_fields
from src.resources.rest_schema.schema_device import device_all_attributes, device_return_attributes, \
    device_all_fields_with_children_base
from src.resources.utils import map_rest_schema

generic_twin_device_all_attributes = deepcopy(device_all_attributes)

generic_twin_device_return_attributes = deepcopy(device_return_attributes)

generic_twin_device_all_fields = {}
map_rest_schema(generic_twin_device_return_attributes, generic_twin_device_all_fields)
map_rest_schema(generic_twin_device_all_attributes, generic_twin_device_all_fields)

generic_twin_device_all_fields_with_children = deepcopy(generic_twin_device_all_fields)
generic_twin_device_all_fields_with_children.update(device_all_fields_with_children_base)
generic_twin_device_all_fields_with_children['points'] = fields.List(fields.Nested(generic_twin_point_all_fields))
