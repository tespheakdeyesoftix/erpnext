import frappe
from frappe.utils import today
from frappe.utils import now


@frappe.whitelist()
def set_system_default_config():

     
    update_system_settings()
    update_website_setting()
    create_uom_unit()
    #update_selling_settings()
    #update_stock_settings()
    #create_webhook()
    #create_customer_display_image()
    #update_company()
    #create_general_customer()
    delete_unuse_uom_conversion()
    delete_unuse_uom()
    delete_unuse_currency()
    create_default_branch()



    #user and permission
    disable_unuse_role()

    create_comment_role()
    create_admin_role()
    create_sync_role_profile()
    create_seller_role_profile()
    create_stock_role_profile()
    create_buyer_role_profile()
    create_stock_and_buyer_role_profile()
    create_sale_and_marketing_role_profile()

    create_admin_role_profile()

    #create module profile
    create_module_profile('Admin Profile',['Core','Desk','Contacts','Buying','Stock','Communication','Bulk Transaction','Printing','CRM','Selling'])
    create_module_profile('Seller Profile',['Desk','Communication','CRM','Selling'])
    create_module_profile('Stock Profile',['Stock','Communication'])
    create_module_profile('Buyer Profile',['Buying','Communication'])
    create_module_profile('Stock and Buyer Profile',['Buying','Communication','Stock'])
    create_module_profile('Sale and Marketing Profile',['CRM','Communication'])
    create_module_profile('Sync Profile',['Communication'])

    
    disable_unuse_stock_entry_type()

    create_wholesale_price_list()
    create_currency_riel()


    #create user
    #create_user(name,full_name,role_profile,module_profile,pos_password,backend_password)
    
    #default pos user
    create_user('cashier','Cashier','Seller Role','Seller Profile','855855','')
    
    #default backend user
    create_user('seller','Seller','Seller Role','Seller Profile','','seller@123')
    create_user('admin','Admin','Admin Role','Admin Profile','855855','admin@123')
    create_user('stock','Stock','Stock Role','Stock Profile','855855','stock@123')
    create_user('buyer','Buyer','Buyer Role','Buyer Profile','855855','buyer@123')
    create_user('stock_mgr','Stock Manager','Stock and Buyer Role','Stock and Buyer Profile','855855','mgr@123')
    create_user('sale','Sale','Sale and Marketing Role','Sale and Marketing Profile','855855','sale@123')
    
    
    

    
    return "Done"
    
def update_system_settings():
    doc = frappe.get_doc('System Settings')
    doc.app_name = 'ePOS Retail'
    doc.enable_onboarding = 0
    doc.system_logo= 'http://webmonitor.inccloudserver.com:1111/epos_retail/asset/epos_retail_app_logo.png'
    doc.pos_date_format = 'dd/mm/yyyy'
    doc.pos_datetime_format = 'dd/MM/yyyy hh:mm:ss tt'
    doc.pos_currency_name ="Dollar"
    doc.pos_currency_symbol="$"
    doc.pos_number_format = "#,###,##0.####"
    doc.pos_second_currency_format = '#,###,##0៛'
    doc.pos_second_currency_symbol='៛'
    doc.pos_second_currency_name ="Riel"
    doc.pos_currency_format = '$#,###,##0.00###'
    doc.first_day_of_the_week = 'Monday'
    doc.allow_login_using_user_name = 1
    doc.enable_password_policy = 0
    doc.disable_system_update_notification = 1
    doc.disable_change_log_notification = 1
    
    doc.save(
        ignore_permissions=True
    )

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


def update_website_setting():
    doc = frappe.get_doc('Website Settings')
    doc.home_page = 'login'
    doc.title_prefix= 'ePOS Retail'
    doc.brand_html = 'EST Computer'
    doc.footer_powered = 'EST Computer'
    doc.app_name = 'ePOS Retail'

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
     if not frappe.db.exists("UOM", {"name": "Unit"}):
        doc = frappe.get_doc({
            "enabled": 1,
            "uom_name": "Unit",
            "must_be_whole_number": 0,
            "doctype": "UOM"
        })
        doc.insert()


def delete_unuse_uom_conversion():
    #delete by category
    datas = frappe.db.get_list('UOM Conversion Factor',
        filters=[[ "category", 'IN', ['Length','Area','Speed','Time','Pressure','Power','Force','Agriculture','Magnetic Induction','Electric Current','Electrical Charge','Frequency and Wavelength','Temperature','Density','Energy']]]
    )
    for d in datas:
        doc = frappe.get_doc('UOM Conversion Factor', d)
        doc.delete()

   
def delete_unuse_uom():
    uoms = [
        'Calibre','Barleycorn','Tesla','Percent','Parts Per Million','Cable Length (UK)','Cable Length (US)','Cable Length','Centimeter','Chain','Decimeter','Ells (UK)','Ems(Pica)','Fathom','Foot','Furlong','Hand','Hectometer','Inch','Kilometer','Link','Micrometer',
        'Mile','Mile (Nautical)','Millimeter','Nanometer','Rod','Vara','Versta','Yard','Arshin','Sazhen','Medio Metro','Square Meter','Centiarea','Area','Manzana','Caballeria','Square Kilometer','Are','Acre','Acre (US)','Hectare','Square Yard','Square Foot','Square Inch','Square Centimeter','Square Mile',
        'Meter/Second','Inch/Minute','Foot/Minute','Inch/Second','Kilometer/Hour','Foot/Second','Mile/Hour','Knot','Mile/Minute','Carat','Cental','Dram','Grain','Hundredweight (UK)','Hundredweight (US)',
        'Quintal','Microgram','Milligram','Ounce','Pood','Pound','Slug','Stone','Tonne','Kip','Barrel(Beer)','Barrel (Oil)','Bushel (UK)','Bushel (US Dry Level)','Centilitre','Cubic Centimeter','Cubic Decimeter',
        'Cubic Foot','Cubic Inch','Cubic Meter','Cubic Millimeter','Cubic Yard','Cup','Decilitre','Fluid Ounce (UK)','Fluid Ounce (US)','Gallon (UK)','Gallon Dry (US)','Gallon Liquid (US)','Millilitre','Peck','Pint (UK)','Pint, Dry (US)','Pint, Liquid (US)','Quart (UK)','Quart Dry (US)','Quart Liquid (US)','Tablespoon (US)','Teaspoon','Day','Hour','Minute','Second','Year','Millisecond',
        'Microsecond','Nanosecond','Week','Atmosphere','Pascal','Bar','Foot Of Water','Hectopascal','Iches Of Water','Inches Of Mercury','Kilopascal','Meter Of Water','Microbar','Mile/Second','Milibar','Millimeter Of Mercury',
        'Millimeter Of Water','Technical Atmosphere','Torr','Dyne','Gram-Force','Joule/Meter','Kilogram-Force','Kilopond','Kilopound-Force','Newton','Ounce-Force','Pond','Pound-Force','Poundal','Tonne-Force(Metric)','Ton-Force (UK)','Ton-Force (US)','Btu (It)','Btu (Th)','Btu (Mean)','Calorie (It)','Calorie (Th)','Calorie (Mean)','Calorie (Food)','Erg','Horsepower-Hours','Inch Pound-Force','Joule','Kilojoule','Kilocalorie','Kilowatt-Hour','Litre-Atmosphere',
        'Megajoule','Watt-Hour','Btu/Hour','Btu/Hour','Btu/Minutes','Btu/Seconds','Calorie/Seconds','Horsepower','Kilowatt','Megawatt','Volt-Ampere','Watt','Centigram/Litre','Decigram/Litre','Dekagram/Litre','Hectogram/Litre','Gram/Cubic Meter','Gram/Cubic Centimeter','Gram/Cubic Millimeter','Gram/Litre','Grain/Gallon (US)','Grain/Gallon (UK)','Grain/Cubic Foot','Kilogram/Cubic Meter','Kilogram/Cubic Centimeter','Kilogram/Litre','Milligram/Cubic Meter','Milligram/Cubic Centimeter','Milligram/Cubic Millimeter','Megagram/Litre','Milligram/Litre','Microgram/Litre','Nanogram/Litre','Ounce/Cubic Inch','Ounce/Cubic Foot','Ounce/Gallon (US)','Ounce/Gallon (UK)','Pound/Cubic Inch','Pound/Cubic Foot','Pound/Cubic Yard','Pound/Gallon (US)','Pound/Gallon (UK)','Psi/1000 Feet','Slug/Cubic Foot','Ton (Short)/Cubic Yard','Ton (Long)/Cubic Yard','Celsius','Fahrenheit','Kelvin','Cycle/Second','Nanohertz','Millihertz','Hertz','Kilohertz','Megahertz','Wavelength In Gigametres','Wavelength In Megametres','Wavelength In Kilometres','Ampere-Hour','Ampere-Minute','Ampere-Second','Coulomb','EMU Of Charge','Faraday','Kilocoulomb','Megacoulomb','Millicoulomb','Nanocoulomb','Ampere','Abampere','Biot','EMU of current','Kiloampere','Milliampere','Gamma','Gauss'
    ]

    #delete by to uom 
    datas = frappe.db.get_list('UOM Conversion Factor',
        filters=[[ "to_uom", 'IN', uoms]]
    )
    for d in datas:
        doc = frappe.get_doc('UOM Conversion Factor', d)
        doc.delete()

    #delete by from uom 
    datas = frappe.db.get_list('UOM Conversion Factor',
        filters=[[ "from_uom", 'IN', uoms]]
    )
    for d in datas:
        doc = frappe.get_doc('UOM Conversion Factor', d)
        doc.delete()

    #delete uom code 
    for d in uoms:
        if frappe.db.exists("UOM", {"name": d}):
            doc = frappe.get_doc('UOM', d)
            doc.delete()


def delete_unuse_currency():
    datas = ['INR','CHF','CNY','JPY','AUD','AED','EUR','GBP','ZWL','ZMW','YER','VND','VEF','VUV','UZS','UYU','UAH','UGX','TMM','TRY','TND','TTD','TOP','THB','TZS','TWD','SYP','SEK','SZL','SRD','LKR','ZAR','SOS','SBD','SGD','SLL','SCR','RSD','SAR','STD','WST','SHP','RWF','RUB','RON','QAR','PLN','PHP','PEN','PYG','PGK','PKR','OMR','NOK','NGN','NIO','NZD','NPR','NAD','MMK','MZN','MAD','MNT','MDL','MXN','MUR','MRO','MVR','MYR','MWK','MKD','MOP','LTL','LYD','LRD','LSL','LBP','LVL','LAK','KGS','KWD','KRW','KPW','KES','KZT','JOD','JMD','ILS','IQD','IRR','IDR','ISK','HUF','HKD','HNL','HTG','GYD','GNF','GTQ','GIP','GHS','GMD','FJD','FKP','ETB','ERN','EGP','DOP','DJF','DKK','CZK','CYP','CUP','HRK','CRC','CDF','KMF','COP','CLP','KYD','CVE','CAD','XAF','BIF','BGN','BND','BRL','BWP','BAM','BOB','BTN','BMD','XOF','BZD','BBD','BDT','BHD','BSD','AWG','AMD','ARS','XCD','KZ','DZD','ALL','AFN']
    for d in datas:
        if frappe.db.exists("Currency", {"name": d}):
            doc = frappe.get_doc('Currency', d)
            doc.delete()

def create_default_branch():
    companies = frappe.db.get_list('Company')
    if len(companies)>0:
        name = companies[0].name
        if not frappe.db.exists("Branch", {"name": name}):
            doc = frappe.get_doc(
                {
                    "branch_code": "01",
                    "branch": name,
                    "doctype": "Branch",
                }
            )
            doc.insert()

def create_comment_role():
    if not frappe.db.exists("Role", {"role_name": "Commenter"}):
            doc = frappe.get_doc(
                {
                   "role_name": "Commenter",
                    "disabled": 0,
                    "is_custom": 0,
                    "desk_access": 1,
                    "two_factor_auth": 0,
                    "search_bar": 1,
                    "notifications": 1,
                    "list_sidebar": 1,
                    "bulk_actions": 1,
                    "view_switcher": 1,
                    "form_sidebar": 1,
                    "timeline": 1,
                    "dashboard": 1,
                    "doctype": "Role"
                }
            )
            doc.insert()

def create_admin_role():
    if not frappe.db.exists("Role", {"role_name": "Admin User"}):
            doc = frappe.get_doc(
                {
                   "role_name": "Admin User",
                    "disabled": 0,
                    "is_custom": 0,
                    "desk_access": 1,
                    "two_factor_auth": 0,
                    "search_bar": 1,
                    "notifications": 1,
                    "list_sidebar": 1,
                    "bulk_actions": 1,
                    "view_switcher": 1,
                    "form_sidebar": 1,
                    "timeline": 1,
                    "dashboard": 1,
                    "doctype": "Role"
                }
            )
            doc.insert()



def create_sync_role_profile():
    if not frappe.db.exists("Role Profile", {"name": "Sync Role"}):
            doc = frappe.get_doc(
                {
                   "role_profile": "Sync Role",
                    "doctype": "Role Profile",
                    "roles": [
                        {
                            "role": "Commenter",
                            "doctype": "Has Role"
                        },
                        {
                            "role": "Sales User",
                            "doctype": "Has Role"
                        },
                        {
                            "role": "Customer",
                            "doctype": "Has Role"
                        },
                        {
                            "doctype": "Has Role",
                            "role": "Accounts User"
                        },
                        {
                            "doctype": "Has Role",
                            "role": "Accounts Manager"
                        },
                        {
                            "doctype": "Has Role",
                            "role": "Sales Manager"
                        }
                    ]
                }
            )
            doc.insert()


def create_seller_role_profile():
    name = "Seller Role"
    if not frappe.db.exists("Role Profile", {"name": name}):
            doc = frappe.get_doc(
                {
                   "role_profile": name,
                    "doctype": "Role Profile",
                    "roles": [
                        {
                            "role": "Commenter",
                            "doctype": "Has Role"
                        },
                        {
                            "role": "Sales User",
                            "doctype": "Has Role"
                        },
                        {
                            "role": "Customer",
                            "doctype": "Has Role"
                        },
                        {
                            "doctype": "Has Role",
                            "role": "Sales Manager"
                        }
                    ]
                }
            )
            doc.insert()    


def create_stock_role_profile():
    name = "Stock Role"
    if not frappe.db.exists("Role Profile", {"name": name}):
            doc = frappe.get_doc(
                {
                    "role_profile": name,
                    "doctype": "Role Profile",
                    "roles": [
                        {
                            "role": "Commenter",
                            "doctype": "Has Role"
                        },
                        {
                            "role": "Item Manager",
                            "doctype": "Has Role"
                        },
                        {
                            "role": "Stock Manager",
                            "doctype": "Has Role"
                        },
                        {
                            "doctype": "Has Role",
                            "role": "Stock User"
                        }
                    ]
                }
            )
            doc.insert()    

def create_buyer_role_profile():
    name = "Buyer Role"
    if not frappe.db.exists("Role Profile", {"name": name}):
            doc = frappe.get_doc({
                "role_profile": name,
                "doctype": "Role Profile",
                "roles": [
                    {
                        "role": "Commenter",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Purchase User",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Purchase Manager",
                        "doctype": "Has Role"
                    }
                ]
            })
            doc.insert()    

def create_stock_and_buyer_role_profile():
    name = "Stock and Buyer Role"
    if not frappe.db.exists("Role Profile", {"name": name}):
            doc = frappe.get_doc({
                "role_profile": name,
                "doctype": "Role Profile",
                "roles": [
                    {
                        "role": "Commenter",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Purchase User",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Item Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Purchase Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Stock Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "doctype": "Has Role",
                        "role": "Stock User"
                    }
                ]
            })
            doc.insert()    


def create_sale_and_marketing_role_profile():
    name = "Sale and Marketing Role"
    if not frappe.db.exists("Role Profile", {"name": name}):
            doc = frappe.get_doc({
                "role_profile": name,
                "doctype": "Role Profile",
                "roles": [
                    {
                        "role": "Commenter",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Customer",
                        "doctype": "Has Role"
                    }
                ]
            })
            doc.insert()    

 
def create_admin_role_profile():
    name = "Admin Role"
    if not frappe.db.exists("Role Profile", {"name": name}):
            doc = frappe.get_doc({
                "role_profile": name,
                "doctype": "Role Profile",
                "roles": [
                    {
                        "role": "Admin User",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Analytics",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Commenter",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Customer",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Dashboard Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Fulfillment User",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Item Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Purchase Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Purchase User",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Report Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Sales Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Sales Master Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Sales User",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Stock Manager",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Supplier",
                        "doctype": "Has Role"
                    },
                    {
                        "role": "Translate",
                        "doctype": "Has Role"
                    },
                    {
                        "doctype": "Has Role",
                        "role": "System Manager"
                    },
                    {
                        "doctype": "Has Role",
                        "role": "Stock User"
                    }
                ]
            })
            doc.insert() 



def disable_unuse_role():
    roles = ['Academics User','Agriculture Manager','Agriculture User','Auditor','Blogger','Employee','Employee Self Service','Expense Approver','Fleet Manager','HR Manager','HR User','Inbox User','Interviewer','Knowledge Base Contributor','Knowledge Base Editor','Leave Approver','Loan Manager','Maintenance Manager','Maintenance User','Manufacturing Manager']
    for r in roles:
        frappe.db.set_value('Role', r, 'disabled', 1, update_modified=False)


def disable_unuse_stock_entry_type():
    data = ['Material Consumption for Manufacture','Material Transfer for Manufacture','Send to Subcontractor','Repack','Manufacture']
    for d in data:
        frappe.db.delete("Stock Entry Type", {
            "name": d
        })


#module profile

def create_module_profile(name, modules):
    if not frappe.db.exists("Module Profile", {"name": name}):
            doc = frappe.get_doc({
                "module_profile_name": name,
                "doctype": "Module Profile",
                "block_modules": get_block_modules(modules)
            })
            doc.insert()   



def create_wholesale_price_list():
     if not frappe.db.exists("Price List", {"name": 'Wholesale Price'}):
            doc = frappe.get_doc({
                "price_list_name": "Wholesale Price",
                "currency": "USD",
                "buying": 0,
                "selling": 1,
                "price_not_uom_dependent": 0,
                "doctype": "Price List"
            })
            doc.insert()   

def create_currency_riel():
     if not frappe.db.exists("Currency", {"name": 'Riel'}):
            doc = frappe.get_doc({
                "currency_name": "Riel",
                "enabled": 1,
                "fraction_units": 1,
                "smallest_currency_fraction_value": 50,
                "symbol": "៛",
                "symbol_on_right": 1,
                "number_format": "#,###",
                "pos_currency_format": "#,###,##0.00##៛",
                "doctype": "Currency"
            })
            doc.insert()   



def get_block_modules(modules):
    block_modules = []
    for m in all_modules():
        if   m not in modules:
            block_modules.append({
                "module": m,
                "doctype": "Block Module"
            })
    return block_modules


def create_user(name,full_name,role_profile,module_profile,pos_password,backend_password):
    
    if not frappe.db.exists("User", {"username": name}):
       
        roles = frappe.get_doc('Role Profile', role_profile).roles
        new_roles = []
        for r in roles:
            new_roles.append({"role":r.role,"doctype":r.doctype})

        doc = frappe.get_doc({
            "doctype":"User",
            "email": name + "@mail.com",
            "first_name": full_name,
            "full_name": full_name,
            "username": name,
            "user_type": "System User",
            "role_profile": role_profile,
            "role_profile_name": role_profile,
            "module_profile": module_profile,
            "language": "en",
            "time_zone": "Asia/Phnom_Penh",
            "send_welcome_email": 0,
            "unsubscribed": 0,
            "allow_login_to_pos": 1,
            "pos_password": pos_password,
            "allow_start_cashier_shift": 1,
            "allow_open_cashdrawer": 1,
            "allow_view_close_receipt": 1,
            "allow_view_shift_report": 1,
            "allow_close_cashier_shift": 1,
            "allow_sale_return_transaction": 1,
            "allow_sale_discount": 1,
            "allow_item_discount": 1,
            "allow_delete_order_item": 1,
            "allow_change_item_price": 1,
            "allow_change_unit": 1,
            "allow_delete_bill": 1,
            "allow_switch_pos_profile": 1,
            "allow_change_price_list_rate": 1,
            "allow_reset_receipt_number_in_current_station": 1,
            "allow_reset_receipt_number_in_all_station": 1,
            "gender": "Male",
            "new_password": backend_password,
            "roles": new_roles
        })
        doc.insert() 
    



def all_modules():
    return ["Core",
            "Website",
            "Workflow",
            "Email",
            "Custom",
            "Geo",
            "Desk",
            "Integrations",
            "Printing",
            "Contacts",
            "Social",
            "Automation",
            "Event Streaming",
            "Accounts",
            "CRM",
            "Buying",
            "Projects",
            "Selling",
            "Setup",
            "HR",
            "Manufacturing",
            "Stock",
            "Support",
            "Utilities",
            "Assets",
            "Portal",
            "Maintenance",
            "Regional",
            "ERPNext Integrations",
            "Quality Management",
            "Communication",
            "Loan Management",
            "Payroll",
            "Telephony",
            "Bulk Transaction",
            "E-commerce",
            "Subcontracting"
        ]

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
        

