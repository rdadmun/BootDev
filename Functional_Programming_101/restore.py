def restore_documents(originals, backups):
    return set(document.upper() for document in originals + backups if not document.isdigit())