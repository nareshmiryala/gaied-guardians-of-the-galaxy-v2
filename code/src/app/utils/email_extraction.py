from win32com.client import Dispatch

def extract_emails_and_attachments(folder_name):
    outlook = Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    folder = namespace.Folders.Item(folder_name)

    emails = []
    attachments = []

    for item in folder.Items:
        if item.Class == 43:  # 43 corresponds to MailItem
            email_details = {
                'subject': item.Subject,
                'body': item.Body,
                'sender': item.SenderName,
                'received_time': item.ReceivedTime
            }
            emails.append(email_details)

            for attachment in item.Attachments:
                attachment_details = {
                    'file_name': attachment.FileName,
                    'file_path': f"C:\\path\\to\\save\\{attachment.FileName}"  # Update path as needed
                }
                attachment.SaveAsFile(attachment_details['file_path'])
                attachments.append(attachment_details)

    return emails, attachments