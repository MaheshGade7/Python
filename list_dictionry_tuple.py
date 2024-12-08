# Simulating a simple database-like structure using list, dictionary, and tuple

# Initialize database-like storage structures
list_db = []  # Simulate database with list
dict_db = {}  # Simulate database with dictionary
tuple_db = []  # Simulate database with tuples


# Function to add a record to the list database
def add_to_list_db(record):
    list_db.append(record)
    print(f"Added to list database: {record}")


# Function to add a record to the dictionary database
def add_to_dict_db(record_id, record_data):
    dict_db[record_id] = record_data
    print(f"Added to dictionary database with ID {record_id}: {record_data}")


# Function to add a record to the tuple database
def add_to_tuple_db(record):
    tuple_db.append(record)
    print(f"Added to tuple database: {record}")


# Function to query the list database
def query_list_db(name):
    result = [record for record in list_db if record["name"] == name]
    return result


# Function to query the dictionary database by ID
def query_dict_db(record_id):
    return dict_db.get(record_id, None)


# Function to query the tuple database by ID
def query_tuple_db(record_id):
    result = [record for record in tuple_db if record[0] == record_id]
    return result


# Main program execution
if __name__ == "__main__":
    # Add records to each database
    add_to_list_db({"id": 1, "name": "Alice", "age": 30})
    add_to_list_db({"id": 2, "name": "Bob", "age": 25})
    add_to_list_db({"id": 3, "name": "Charlie", "age": 35})

    add_to_dict_db(1, {"name": "Alice", "age": 30})
    add_to_dict_db(2, {"name": "Bob", "age": 25})
    add_to_dict_db(3, {"name": "Charlie", "age": 35})

    add_to_tuple_db((1, "Alice", 30))
    add_to_tuple_db((2, "Bob", 25))
    add_to_tuple_db((3, "Charlie", 35))

    # Display the contents of all databases
    print("\nList Database Contents:")
    for record in list_db:
        print(record)

    print("\nDictionary Database Contents:")
    for key, value in dict_db.items():
        print(f"ID: {key}, Data: {value}")

    print("\nTuple Database Contents:")
    for record in tuple_db:
        print(record)

    # Query data
    query_name = "Alice"
    print(f"\nQuery List Database for name='{query_name}':")
    print(query_list_db(query_name))

    query_id = 2
    print(f"\nQuery Dictionary Database for id={query_id}:")
    print(query_dict_db(query_id))

    print(f"\nQuery Tuple Database for id={query_id}:")
    print(query_tuple_db(query_id))
