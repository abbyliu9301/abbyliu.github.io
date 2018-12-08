import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # input is a 2-element list: [document_id, text]
    # key: text
    # value: document_id
    document_id = record[0]
    text = record[1]
    words = text.split()
    for w in words:
        mr.emit_intermediate(w, document_id)

def reducer(key, values):
    # key: word
    # values: list of document_id
    id_list = list(set(values))
    mr.emit((key, id_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
