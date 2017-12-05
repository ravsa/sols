#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert normal JSON to tree-table JSON format."""
import json


def cast_dict(key, value):
    """Casting normal JOSN object to tree table acceptable JSON."""
    if isinstance(value, str) or isinstance(value,
                                            bool) or isinstance(value, int):
        return {'data': {
            "key": key,
            "value": value
        }}
    elif isinstance(value, dict):
        return {
            "data": {
                "key": key
            },
            "children": [cast_dict(*d) for d in value.items()]
        }
    elif isinstance(value, list):
        return {
            "data": {
                "key": key
            },
            "children": [cast_dict(str(i), d) for i, d in enumerate(value)]
        }


def main(input_json, output_json):
    "Main function."
    json_object = {"data": list()}
    for key, value in json.load(open(input_json)).items():
        json_object['data'].append(cast_dict(key, value))
    json.dump(json_object, open(output_json, 'w'), indent=4)


if __name__ == "__main__":
    main('oc_.json', 'output.json')
