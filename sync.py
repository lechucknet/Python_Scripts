## Folder Sync - Fraud & Sharepoint
## gonzaloanavarro@gmail.com 

import os
import office365
from office365.sharepoint.caml_query import CamlQuery
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.file import File
from office365.sharepoint.file_creation_information import FileCreationInformation


def read_folder_and_files_alt(context, list_title):
    """Read a folder example"""
    list_obj = context.web.lists.get_by_title(list_title)
    qry = CamlQuery.create_all_items_query()
    items = list_obj.get_items(qry)
    context.execute_query()
    for cur_item in items:
        print("File name: {0}".format(cur_item.properties["Title"]))


def read_folder_and_files(context, list_title):
    """Read a folder example"""
    list_obj = context.web.lists.get_by_title(list_title)
    folder = list_obj.rootFolder
    context.load(folder)
    context.execute_query()
    print("List url: {0}".format(folder.properties["ServerRelativeUrl"]))

    files = folder.files
    context.load(files)
    context.execute_query()
    for cur_file in files:
        print("File name: {0}".format(cur_file.properties["Name"]))

    folders = context.web.folders
    context.load(folders)
    context.execute_query()
    for folder in folders:
        print("Folder name: {0}".format(folder.properties["Name"]))


def upload_file(context):
    path = "../../tests/data/SharePoint User Guide.docx"
    with open(path, 'rb') as content_file:
        file_content = content_file.read()

    list_title = "Documents"
    target_folder = context.web.lists.get_by_title(list_title).rootFolder
    info = FileCreationInformation()
    info.content = file_content
    info.url = os.path.basename(path)
    info.overwrite = True
    target_file = target_folder.files.add(info)
    context.execute_query()
    print("File url: {0}".format(target_file.properties["ServerRelativeUrl"]))


def download_file(context):
    path = "../../tests/data/SharePoint User Guide.docx"
    response = File.open_binary(context, "Shared Documents/SharePoint User Guide.docx")
    response.raise_for_status()
    with open(path, "wb") as local_file:
        local_file.write(response.content)


if __name__ == '__main__':
    
    site_url = 'https://office365-my.sharepoint.com/personal/*put your user here*/_layouts/15/onedrive.aspx'
    
    # User  credentials 
    username = 'put your user here'
    password = 'put your password here'
    
    # Auth
    #context_auth = AuthenticationContext(url=settings[site_url])
    #if context_auth.acquire_token_for_user(username=settings['user_credentials']['username'],
    #                                       password=settings['user_credentials']['password']):
    
    # Execute command
    ctx = ClientContext.connect_with_credentials(site_url, UserCredential(settings['user_credentials'][username],
                                                                          settings['user_credentials'][password]))
   
   

    # upload_file(ctx)
    #download_file(ctx)
    read_folder_and_files(ctx)
    # get a source file located in library 'Shared Documents'
    # source_file = ctx.web.get_file_by_server_relative_url("/teams/DemoSite/Shared Documents/Guide.docx")
    # move a file into sub folder called 'Archive'
    # source_file.moveto("/teams/DemoSite/Shared Documents/Archive/Guide.docx", 1)
    # execute a query
    # ctx.execute_query()
