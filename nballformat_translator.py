
##./data/mappings/apple-senses.mapping
## file path via console or replace input() with the path itself

def extract_glove_embeddings (mapping):
    with open("./data/glove.6B.50d.txt",'r', encoding='utf-8') as gl:
        glove = gl.read().splitlines() 
        for i in range(len(glove)):
            glove [i] = glove[i].split()
        extracted_glove_lines= []
        mapping_string = " "
        for i in range(len(mapping)):
            mapping_string = mapping[i][0].partition(".")[0] ##e.g. apple, entity, etc.
            found = False
            idx = 0
            while(not found ) or (idx==len(glove)):
                found_string = ""
                if(glove[idx][0].find(mapping_string) == 0):
                    found_string = glove[idx][0]
                if(found_string != mapping_string):
                    idx += 1
                else:
                    extracted_glove_lines.append(glove[idx])
                    found=True
        return extracted_glove_lines



with open(input("Mapping File: "),'r') as m:
    mapping = m.read().splitlines()
    for i in range(len(mapping)):
        mapping[i] = mapping[i].split(" ")
    ##./data/emb/as2.emb
    with open(input("Embedding File: "),'r') as emb:
        embedding = emb.read().splitlines()
        with open("./data/glove.6B.50d.txt",'r', encoding='utf-8') as gl:
            glove = gl.read().splitlines()
            glove_embedding = extract_glove_embeddings(mapping)
            with open ("translated_embedding.emb", 'w+') as f:
                embedding.pop(0)
                for i in range(len(embedding)):
                    embedding[i] = embedding[i].split(",")
                    embedding[i].pop(len(embedding[i])-1)
                    embedding[i][0] = embedding[i][0].replace(embedding[i][0],mapping[i][0])
                    f.write(" ".join(embedding[i]) + " ".join(glove_embedding[i]) + "\n")


                 
                   

                    
      
            