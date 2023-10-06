def report_to_list(report):
    report_list = {
        'id'          : report.id,
        'title'       : report.title,
        'description' : report.description,
        'likes'       : report.likes,
        'date'        : report.date,
        'id_product'  : report.id_product,
        'id_priority' : report.id_priority,
        'id_state'    : report.id_state,
        'id_developer': report.id_developer
    }
    
    return report_list

def product_to_list(product):
    product_list = {
        'id'          : product.id,
        'name'        : product.name,
        'id_developer': product.id_developer
    }
    
    return product_list

def developer_to_list(developer):
    developer_list = {
        'id'     : developer.id,
        'name'   : developer.name,
        'email'  : developer.email,
        'id_role': developer.id_role
    }
    
    return developer_list

def state_to_list(state):
    state_json = {
        'id' : state.id,
        'name' : state.name,
    }
    return state_json

def comment_to_list(comment):
    comment_json = {
        'id': comment.id,
        'content': comment.content,
        'date': comment.date
    }
    return comment_json

def priority_to_list(priority):
    priority_json = {
        'id': priority.id,
        'name': priority.name
    }
    return priority_json