#!/usr/bin/env python3
import json
from flask import Response, Flask, request

import inspect
from typecheck import typecheck
from typing import (
                    List,
                    Dict)


def typed_service(func):
    def service():
        print(request.json)
        print(type(request.json))
        args_dict: Dict = request.json
        arg_inspect = inspect.getfullargspec(func)
        # if the function accepts an additional dictionary of arbitrary items, accept unknown arguments
        if arg_inspect.varkw is None:
            for k in args_dict.keys():
                if k not in func.__annotations__:
                    return Response(json.dumps({
                        "invalid_argument_name": k,
                        "error": "unknown argument name"
                    }), status=400, mimetype='application/json')
        for (arg_name, arg_type) in func.__annotations__.items():
            if arg_name == 'return':
                continue
            if not typecheck.check_type(args_dict[arg_name], arg_type):
                return Response(json.dumps({
                    "invalid_argument_name": arg_name,
                    "error": "invalid type",
                    "expected_type": str(arg_type),
                    "received_value": args_dict[arg_name]
                }), status=400, mimetype='application/json')
        js = json.dumps(func(**request.json))
        resp = Response(js, status=200, mimetype='application/json')

        return resp

    return service


app = Flask(__name__)




@app.route('/bark_typed', methods=['POST'])
@typed_service
def bark(name: str, number_of_barks: int = 3, friends: List[str] = []) -> Dict:
    return {'number of barks': number_of_barks,
            'bark message': ' '.join(([name, "woof!"] * number_of_barks)),
            'my friends are': friends
            }


@app.route('/bark', methods=['POST'])
def api_bark():
    js = json.dumps(bark("William", 4))

    resp = Response(js, status=200, mimetype='application/json')

    return resp

if __name__ == '__main__':
    app.run()
