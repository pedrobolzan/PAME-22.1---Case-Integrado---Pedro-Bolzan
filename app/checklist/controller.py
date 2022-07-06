from app.checklist.model import Checklist
from flask import request, jsonify
from flask.views import MethodView

class ChecklistCreate(MethodView): # rota = /registroChecklist

    def post (self):

        body = request.json

        id = body.get("id")
        agendamento = body.get("agendamento")
        cadastro = body.get("cadastro")
        checkin = body.get("checkin")
        triagem = body.get("triagem")
        consulta = body.get("consulta")
        checkout = body.get("checkout")
        limpeza = body.get("limpeza")

        if isinstance(agendamento, str) and\
            isinstance(cadastro, str) and\
                isinstance(checkin, str) and\
                    isinstance(triagem, str) and\
                        isinstance(consulta, str) and\
                            isinstance(checkout, str) and\
                                isinstance(limpeza, str):
            
            checklist1 = Checklist.query.filter_by(agendamento = agendamento).first()
            
            if checklist1:
                return {"code_status": "Dados inválidos, etapa já cadastrada"}, 400

            checklist1 = Checklist(agendamento=agendamento,
                                      cadastro=cadastro,
                                      checkin=checkin,
                                      triagem=triagem,
                                      consulta=consulta,
                                      checkout=checkout,
                                      limpeza=limpeza)

            checklist1.save()

            return checklist1.json(), 200

    def get (self):

        checklists = Checklist.query.all()

        return jsonify([checklist.json() for checklist in checklists]), 200

class ChecklistDetails (MethodView): #rota = /modificarChecklist/<id>

    def get (self, id):

        checklist = Checklist.query.get_or_404(id)

        return checklist.json()

    def put (self, id):

        body = request.json
        checklist = Checklist.query.get_or_404(id)

        id = body.get("id")
        agendamento = body.get("agendamento")
        cadastro = body.get("cadastro")
        checkin = body.get("checkin")
        triagem = body.get("triagem")
        consulta = body.get("consulta")
        checkout = body.get("checkout")
        limpeza = body.get("limpeza")

        if isinstance(agendamento, str) and\
            isinstance(cadastro, str) and\
                isinstance(checkin, str) and\
                    isinstance(triagem, str) and\
                        isinstance(consulta, str) and\
                            isinstance(checkout, str) and\
                                isinstance(limpeza, str):

            checklist.agendamento = agendamento
            checklist.cadastro = cadastro
            checklist.checkin = checkin
            checklist.triagem = triagem
            checklist.consulta = consulta
            checklist.checkout = checkout
            checklist.limpeza = limpeza

            checklist.update()

            return checklist.json(), 200
        else:
            return {"code_status": "dados inválidos"}, 400
    
    def patch (self, id):

        body = request.json
        checklist = Checklist.query.get_or_404(id)

        id = body.get("id")
        agendamento = body.get("agendamento", checklist.agendamento)
        cadastro = body.get("cadastro", checklist.cadastro)
        checkin = body.get("checkin", checklist.checkin)
        triagem = body.get("triagem", checklist.triagem)
        consulta = body.get("consulta", checklist.consulta)
        checkout = body.get("checkout", checklist.checkout)
        limpeza = body.get("limpeza", checklist.limpeza)

        if isinstance(agendamento, str) and\
            isinstance(cadastro, str) and\
                isinstance(checkin, str) and\
                    isinstance(triagem, str) and\
                        isinstance(consulta, str) and\
                            isinstance(checkout, str) and\
                                isinstance(limpeza, str):

            checklist.agendamento = agendamento
            checklist.cadastro = cadastro
            checklist.checkin = checkin
            checklist.triagem = triagem
            checklist.consulta = consulta
            checklist.checkout = checkout
            checklist.limpeza = limpeza

            checklist.update()

            return checklist.json(), 200
    
    def delete (self, id):

        checklist = Checklist.query.get_or_404(id)
        checklist.delete(checklist)

        return checklist.json()