
#ณัฐชนน คงแก้ว 6430110921
#(1)
# Sorting Transaction by timestamp
def sorting_transaction(transaction_list):
    lst = []
    for i in range (len(transaction_list)) :
        timestamp = transaction_list[i][3]
        acc_name_from = transaction_list[i][0]
        acc_name_to = transaction_list[i][1]
        amount = transaction_list[i][2]
        hash =transaction_list[i][4]
        lst.append([timestamp,acc_name_from, acc_name_to, amount,hash,i])
    lst.sort()
    out = []
    for e in lst :
        out.append([e[1],e[2],e[3],e[0],e[4]])

    return out

# (2)
# Hash all transaction into one hash string
def hash_transaction_list(transaction_list):
    k = sorting_transaction(transaction_list)
    str_hash_joint = ''
    for e in k :
        str_hash_joint += (e[4])
    return hash_sha256(str_hash_joint)


# (3)
# Update the ledger from transaction_list

def update_ledger(ledger, transaction_list):
    txt_sort = sorting_transaction(transaction_list)
    ledg_new = copy_list(ledger)
    for txn_data in txt_sort:
        if txn_data[0] == "0"*64:
            check1_lg = 0
            for i in range(len(ledg_new)):
                if txn_data[1] == ledg_new[i][0]:
                    ledg_new[i][1] += txn_data[2]
                    check1_lg = 1
                    break
            if check1_lg == 0:
                ledg_new.append([txn_data[1], txn_data[2]])
        else:
            check1_lg = 0
            for i in range(len(ledg_new)):
                if txn_data[0] == ledg_new[i][0]:
                    if ledg_new[i][1] - txn_data[2] < 0:
                        return [ledger, [False, txn_data]]
                    else:
                        ledg_new[i][1] -= txn_data[2]
                        check2_lg = 0
                        for j in range(len(ledg_new)):
                            if txn_data[1] == ledg_new[j][0]:
                                ledg_new[j][1] += txn_data[2]
                                check2_lg = 1
                                break
                        if check2_lg == 0:
                            ledg_new.append([txn_data[1], txn_data[2]])
                    check1_lg = 1
                    break
            if check1_lg == 0:
                return [ledger, [False, txn_data]]
    return [ledg_new, [True,[]]]


#(4)
def sorting_block(block_list):  #คืน b3->b5->b1->b2->b4
    #block == create_block(transaction_list, prev_hash)
    arrange_box = []
    kk = False
    for i in range(len(block_list)) :
        Pre_hash = block_list[i][2]
        for j in range(len(block_list)) :
            Next_hash = block_list[j][3]
            last = len(block_list)-1
            if Pre_hash == Next_hash:
                break
            elif block_list[i][2] != block_list[j][3] and j == last:
                arrange_box.append(block_list[i])
    for k in range(len(block_list)-1) :
        next_hash = arrange_box[len(arrange_box)-1][3]
        for i  in range(len(block_list)):
            pre_hash = block_list[i][2]
            if pre_hash == next_hash:
                arrange_box.append(block_list[i])
                break
    return arrange_box           
   
# (5)
# Check the chain that transaction is valid to what number block
def maximum_valid_block(block_list): #คืนจำนวนchainที่ถูก
    count = 0
    ledger_x = []
    sort_chain = sorting_block(block_list)
    for m in range(len(sort_chain)):
        transitionlst = sort_chain[m][0]
        update_ledger_now = update_ledger(ledger_x, transitionlst)
        can_continue = update_ledger_now[1][0]  #true false
        if can_continue == False :
            return count
        elif can_continue == True:
            count += 1
            ledger_x = copy_list(update_ledger_now[0])
    return count

# (6)
# check ledger in the block no. if before block no the block is not valid return the ledger to block that valid
def block_ledger(block_list, block_no): 
    if block_no > 0  :
        ledger_txn = []
        num_valid_block =  maximum_valid_block(sorting_block(block_list))
        blocklist_arrange = sorting_block(block_list)
        for e in range(block_no) :
            update_led = update_ledger(ledger_txn,blocklist_arrange[e][0])
            ledger_txn = update_led[0]
            ledger_t_f = update_led[1][0]
            if num_valid_block < block_no and ledger_t_f == False :
                return [ledger_txn, num_valid_block]        
        if num_valid_block >= block_no  :
            return [ledger_txn,block_no]
    elif block_no == 0 :
        return [[],0]

