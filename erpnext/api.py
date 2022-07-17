import frappe
from frappe.utils import today
from frappe.utils import now


@frappe.whitelist()
def set_system_default_config():
    create_uom_unit()
    #update_selling_settings()
    #update_stock_settings()
    #create_webhook()
    #create_customer_display_image()
    #update_company()
    #create_general_customer()
    
    return "Done"
    

def update_selling_settings():
    doc = frappe.get_doc('Selling Settings')
    doc.cust_master_name = 'Naming Series'
    doc.save(
        ignore_permissions=True
    )

def update_stock_settings():
    doc = frappe.get_doc('Stock Settings')
    doc.item_naming_by = 'Item Code'
    doc.stock_uom = 'Unit'
    doc.allow_negative_stock = 1

    doc.save(
        ignore_permissions=True
    )

def update_company():
    companies = frappe.db.get_list('Company')
    if len(companies)>0:
        name = companies[0].name
        doc = frappe.get_doc('Company',name)
        doc.phone_no = "0123456789"
        doc.address = "Siemreap, Cambodia"
        doc.company_logo = "http://webmonitor.inccloudserver.com:1111/epos_retail/asset/retaillogo.png"
        doc.pos_background_image = "http://webmonitor.inccloudserver.com:1111/epos_retail/asset/bg01.jpg"
        doc.pos_customer_display_thank_you_background = "http://webmonitor.inccloudserver.com:1111/epos_retail/asset/thank.jpg"

     
        if not any(d.get('image') == 'slideshow1' for d in doc.customer_display_slideshow):
            doc.append("customer_display_slideshow", {
                "image":"slideshow1",
            })
        
        if not any(d.get('image') == 'slideshow2' for d in doc.customer_display_slideshow):
            doc.append("customer_display_slideshow", {
                "image":"slideshow2",
            })
        
        if not any(d.get('image') == 'slideshow3' for d in doc.customer_display_slideshow):
            doc.append("customer_display_slideshow", {
                "image":"slideshow3",
            })
        
        if not any(d.get('image') == 'slideshow4' for d in doc.customer_display_slideshow):
            doc.append("customer_display_slideshow", {
                "image":"slideshow4",
            })
        
        


        
        doc.save()    

def create_customer_display_image():
    if not frappe.db.exists("Image Galleries", {"name": "slideshow1"}):
        doc = frappe.get_doc({
            "doctype": "Image Galleries",
            "image":"http://webmonitor.inccloudserver.com:1111/epos_retail/asset/slideshow1.jpg",
            "description":"slideshow1"
        })
        doc.insert()

    if not frappe.db.exists("Image Galleries", {"name": "slideshow2"}):
        doc = frappe.get_doc({
            "doctype": "Image Galleries",
            "image":"http://webmonitor.inccloudserver.com:1111/epos_retail/asset/slideshow2.jpg",
            "description":"slideshow2"
        })
        doc.insert()
    
    if not frappe.db.exists("Image Galleries", {"name": "slideshow3"}):
        doc = frappe.get_doc({
            "doctype": "Image Galleries",
            "image":"http://webmonitor.inccloudserver.com:1111/epos_retail/asset/slideshow3.jpg",
            "description":"slideshow3"
        })
        doc.insert()
    if not frappe.db.exists("Image Galleries", {"name": "slideshow4"}):
        doc = frappe.get_doc({
            "doctype": "Image Galleries",
            "image":"http://webmonitor.inccloudserver.com:1111/epos_retail/asset/slideshow4.jpg",
            "description":"slideshow4"
        })
        doc.insert()
    

def create_general_customer():
    if not frappe.db.exists("Customer", {"name": "General Customer"}):
        doc = frappe.get_doc({
            "name":"General Customer",
            "customer_name": "General Customer",
            "customer_group": "All Customer Groups",
            "customer_type": "Individual",
            "territory": "Cambodia",
            "doctype": "Customer",
        })
        doc.insert()


def create_uom_unit():
     if not frappe.db.exists("UOM", {"name": "Unitx"}):
        doc = frappe.get_doc({
            "enabled": 1,
            "uom_name": "Unitx",
            "must_be_whole_number": 0,
            "doctype": "UOM"
        })
        doc.insert()

def create_webhook():
    url = "http://192.168.10.28:5224/api/sync/UpdateRecord"

    if not frappe.db.exists("Webhook", {"webhook_doctype": "Comment"}):
        doc = frappe.get_doc({
            "naming_series": "HOOK-.####",
            "title": "Document Rename, Delete",
            "webhook_doctype": "Comment",
            "webhook_docevent": "after_insert",
            "enabled": 1,
            "condition": "doc.reference_doctype ==\"Item\" or doc.reference_doctype ==\"Item Group\" or doc.reference_doctype ==\"Item Price\" or doc.reference_doctype ==\"Customer\" or doc.reference_doctype ==\"Customer Group\"  or doc.reference_doctype ==\"User\" or doc.reference_doctype ==\"POS Profile\" or doc.reference_doctype==\"Company\" or doc.reference_doctype==\"System Settings\" or doc.reference_doctype==\"Currency Exchange\" or doc.reference_doctype==\"Warehouse\" or doc.reference_doctype==\"Membership Type\"",
            "request_url": url,
            "request_method": "POST",
            "request_structure": "Form URL-Encoded",
            "enable_security": 0,
            "doctype": "Webhook",
            "webhook_data": [
                {
                    "fieldname": "reference_doctype",
                    "key": "doctype"
                },
                {
                    "fieldname": "reference_name",
                    "key": "name"
                },
                {
                    "fieldname": "content",
                    "key": "content"
                },
                {
                    "fieldname": "subject",
                    "key": "subject"
                },
                {
                    "fieldname": "comment_type",
                    "key": "comment_type"
                }
            ],
            "webhook_headers": [
                {
                    "key": "Content-Type",
                    "value": "application/x-www-form-urlencoded"
                }
            ]
        })
        doc.insert()

    if not frappe.db.exists("Webhook", {"webhook_doctype": "Version"}):
        doc = frappe.get_doc({
            "naming_series": "HOOK-.####",
            "title": "Document Created, Update",
            "webhook_doctype": "Version",
            "webhook_docevent": "after_insert",
            "enabled": 1,
            "condition": "doc.ref_doctype ==\"Item\" or doc.ref_doctype ==\"Item Group\" or doc.ref_doctype ==\"Item Price\" or doc.ref_doctype ==\"Customer\" or doc.ref_doctype ==\"Customer Group\"  or doc.ref_doctype ==\"User\" or doc.ref_doctype ==\"POS Profile\" or doc.ref_doctype==\"Company\" or doc.ref_doctype==\"System Settings\" or doc.ref_doctype==\"Currency Exchange\" or doc.ref_doctype==\"Warehouse\"  or doc.ref_doctype==\"Membership Type\"",
            "request_url":url,
            "request_method": "POST",
            "request_structure": "Form URL-Encoded",
            "enable_security": 0,
            "doctype": "Webhook",
            "webhook_data": [
                {
                    "fieldname": "name",
                    "key": "name"
                },
                {
                    "fieldname": "ref_doctype",
                    "key": "doctype"
                }
            ],
            "webhook_headers": [
                {
                    "key": "Content-Type",
                    "value": "application/x-www-form-urlencoded"
                }
            ]
        })
        doc.insert()
        



         




    
 

