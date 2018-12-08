import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # input is a 2 element list [sequence id, nucleotides]
    id = record[0]
    nucleo = record[1]
    mr.emit_intermediate(nucleo[:-10], id)

def reducer(key,record):
    # key: sequence id
    # record: nucle
    mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
