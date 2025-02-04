def new_collection(initial_docs):
    copy_docs = initial_docs.copy()
    def copy_collection(new_docs):
        copy_docs.append(new_docs) 
        return copy_docs
    return copy_collection
