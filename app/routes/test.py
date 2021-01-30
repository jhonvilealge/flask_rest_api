from flask import Blueprint
from ..services import test

# Create blueprint
bp_test = Blueprint('test', __name__)

# Create a test
@bp_test.route('/api/test', methods=['POST'])
def post_test():
    return test.post_test()

# Get all tests
@bp_test.route('/api/test', methods=['GET'])
def get_tests():
    return test.get_tests()

# Get a single test
@bp_test.route('/api/test/<test_id>', methods=['GET'])
def get_test(test_id):
    return test.get_test(test_id)

# Delete a test
@bp_test.route('/api/test/<test_id>', methods=['DELETE'])
def delete_test(test_id):
    return test.delete_test(test_id)
