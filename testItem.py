from tree import Tree
import mysql.connector
import json

config = {
    'user' : 'root',
    'password' : '',
    'host' : 'localhost',
    'database' : 'test',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT * FROM imm_web_node_relation ")

cursor.execute(query)

(_ROOT, _DEPTH, _BREADTH) = range(3)

tree = Tree()
for (parent, child) in cursor:
    print("parent: {}, child: {}".format(parent, child))
    
    try:
        tree[parent]
    except KeyError:
        tree.add_node(parent)
        
    try:
        tree[child]
    except KeyError:
        tree.add_node(child)
        
    tree[parent].add_child(child)
    tree[child].add_parent(parent)


query = ("SELECT id, name FROM imm_web")
cursor.execute(query)
id_name_dict = {}
for (id, name) in cursor:
    id_name_dict[id] = name

tree.display(1)
return_info = dict()
print("***** DEPTH-FIRST ITERATION *****")
for node in tree.traverse(1):
    print(str(node) + ", " + id_name_dict[node] + ", " + str(tree[node].parent))
    return_info[node] = [id_name_dict[node], tree[node].parent]
print("***** BREADTH-FIRST ITERATION *****")
for node in tree.traverse(1, mode=_BREADTH):
    print(str(node) + ", " + id_name_dict[node])

cursor.close()
cnx.close()