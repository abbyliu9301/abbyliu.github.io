import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # input is a 2-element list: [personA, personB]
    # B is a friend of A, the opposite may not be necessarily true
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, 1)

def reducer(key, values):
    # key: person
    # values: friend count
    friend = 0
    for v in values:
        friend += v
    mr.emit((key, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
