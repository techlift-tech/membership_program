// Copyright (c) 2019, Techlift and contributors
// For license information, please see license.txt

function get_categories(frm){
    if(frm.doc.membership_program){
        frappe.db.get_doc('Membership Program', frm.doc.membership_program)
            .then(function(r){
                var category_options = []
                for(var category of r.membership_program_categories){
                    category_options.push(category.category_name)
                }
                frm.set_df_property('category', 'options', category_options)
            }).catch(function(e){
                frappe.msgprint(e)
            })
    }
}

frappe.ui.form.on('Membership Card', {
    refresh: function(frm) {
        get_categories(frm)
    },
    membership_program: function(frm) {
        get_categories(frm)
    }
});
