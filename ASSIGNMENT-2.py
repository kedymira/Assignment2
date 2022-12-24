#!/usr/bin/env python
# coding: utf-8

# In[21]:


x = open("/home/ergunb/shared_folder/MOBG2143/assignment_2/16s_database.fasta", 'r')

file_lines = x.readlines()

x.close()


# In[22]:


seq_id = []
sequence = str()
sequence_array = []

dict_seq_id_seq = {}

for k in file_lines:
    if ">" in k:
        seq_id.append(k)
for k in file_lines:
    if ">" in k:
        sequence_array.append(sequence)
        sequence = str()
    else:
        sequence = sequence +k
        
sequence_array.append(sequence)

del sequence_array[0]

for k in range(len(seq_id)):
    seq_id[k] = seq_id[k].replace('\n' , "")
    
for k in range (len(seq_id)):
    seq_id[k] = seq_id[k].replace('\n' , "")
    
for k in range(len(sequence_array)):
    sequence_array[k] = sequence_array[k].replace('\n' , "")
    
# This line was done by Eslem and Ezgi


# In[23]:


array_extracted = []
array_extracted2 = []
stop_codons = ["UAG", "UAA", "UGA"]
start_codon = ["AUG"]

start_codons = []

for k in range(len(sequence_array)):
    to_be_extracted = sequence_array[k]
    start_codon_position = []
    stop_codon_positions = []

    n = len(to_be_extracted)
    m = 0

    while m < n - 2:
        # extract a three-nucleotide subsequence
        possible_codon = to_be_extracted[m:m + 3]
        if possible_codon in start_codon:
            start_codon_position.append(m)
            break
        m = m+1


    ind = start_codon_position[0]+3
    while ind < n - 2:
        possible_codon = to_be_extracted[ind:ind + 3]
        if possible_codon in stop_codons:
            stop_codon_positions.append(ind)
            break
        ind = ind + 1

    array_extracted.append(to_be_extracted[start_codon_position[0]:stop_codon_positions[0] + 3])
    array_extracted2.append(to_be_extracted[start_codon_position[0] + 3:stop_codon_positions[0]])
    
    
    # This line was written by Bahar and Nilay


# In[24]:


coding_region = str()

for k in range(len(seq_id)):
    coding_region = coding_region+seq_id[k] + "\n" + array_extracted[k] +"\n"


# In[25]:


save_coding_region = open(r'/home/ergunb/codding_reagion.fasta', 'w+')
save_coding_region.write(coding_region)
save_coding_region.close()


# In[26]:


coding_region1 = str()

for k in range(len(seq_id)):
    coding_region1 = coding_region1+seq_id[k] + "\n" + array_extracted2[k] +"\n"
    
# This line was done by Eslem and Ezgi


# In[27]:


# save_coding_region = open(r'/home/tascib/coding_region_without_start_stop_codons.fasta', 'w+')
# save_coding_region.write(coding_region1)
# save_coding_region.close()


# In[28]:


coding_region_lengths = []

for k in range(len(array_extracted2)):
    coding_region_lengths.append(len(array_extracted2[k]))


# In[29]:


sequence_identifiers = []

for k in range(len(seq_id)):
    id = seq_id[k].split(" ")
    id = id[0]
    
    sequence_identifiers.append(id[1:])


# In[30]:


len(sequence_identifiers)


# In[31]:


zip_iterator = zip(sequence_identifiers, coding_region_lengths)
dict_lengths = dict(zip_iterator)


# In[32]:


import pickle 


with open(r'/home/ergunb/lengths.pkl','wb') as handle:
    pickle.dump(dict_lengths, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(r'/home/ergunb/lengths.pkl', 'rb') as handle:
    lengths = pickle.load(handle)

print(dict_lengths == lengths)


# In[33]:


import pickle

f = open(r'/home/ergunb/lengths.pkl','wb')
pickle.dump(dict_lengths,f)
f.close()


# In[34]:


sequence_identifiers2 = []
domain_phylum_class = []

for k in range(len(seq_id)):
    id = seq_id[k].split(" ")
        
    sequence_identifiers2.append(id[1])

for k in range(len(sequence_identifiers2)):
    three_fields = sequence_identifiers2[k].split(";")
    domain_phylum_class.append(three_fields[0:3])

# This line was done by Ekin


# In[35]:


zip_iterator2 = zip(sequence_identifiers, domain_phylum_class)
dict_columns = dict(zip_iterator2)


# In[36]:


import csv
with open(r'/home/ergunb/tsvfile_bahar.tsv', 'wt') as file:
    tsv_writer = csv.writer(file, delimiter = '\t')
    tsv_writer.writerow(['SequenceID', 'Domain', 'Phylum', 'Class'])
    
    for k in range(len(sequence_identifiers)):
        argument1 = []
        
        argument1.append(sequence_identifiers[k])
        argument1.append(domain_phylum_class[k][0])
        argument1.append(domain_phylum_class[k][1])
        if len(domain_phylum_class[k])>2:
            argument1.append(domain_phylum_class[k][2])
        else:
            pass
     
        
        tsv_writer.writerow(argument1)
        
# This line was done by Nilay, Bahar, and Ekin


# In[37]:


len(sequence_identifiers)


# In[38]:


x = open(r'/home/ergunb/tsvfile_bahar.tsv', 'r')

file_lines = x.readlines()

x.close()


# In[39]:


len(file_lines)


# In[ ]:




