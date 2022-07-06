from app.checklist.model import checklist_api
from app.checklist.controller import ChecklistCreate, ChecklistDetails

checklist_api.add_url_rule("/registroChecklist", view_func= ChecklistCreate.as_view("cria_checklist"), methods = ["POST","GET"])
checklist_api.add_url_rule("/modificarChecklist/<id>", view_func= ChecklistDetails.as_view("modifica_checklist"), methods = ["GET","PUT","PATCH","DELETE"])