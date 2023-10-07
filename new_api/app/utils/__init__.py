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
        'id_developer': report.id_developer,
        'id_user'     : report.id_user
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