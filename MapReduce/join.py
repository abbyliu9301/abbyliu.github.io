import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # first item identify the table: line_item or order
    # second item is the order_id
    table = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id,record)

def reducer(key,record):
    # key: order_id
    # record
    for v in record:
        if v[0] == 'order':
            for v1 in record:
                if v1[0] == 'line_item':
                    mr.emit(v + v1)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
