"""empty message

Revision ID: 25b82a12a4cf
Revises: 
Create Date: 2022-07-06 15:45:03.441139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25b82a12a4cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agendamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nomeResponsavel', sa.String(length=100), nullable=True),
    sa.Column('nomeCrianca', sa.String(length=100), nullable=True),
    sa.Column('nascimento', sa.String(length=100), nullable=True),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('data', sa.String(length=100), nullable=True),
    sa.Column('horario', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('data'),
    sa.UniqueConstraint('horario'),
    sa.UniqueConstraint('nomeCrianca')
    )
    op.create_table('checklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agendamento', sa.Boolean(), nullable=True),
    sa.Column('cadastro', sa.Boolean(), nullable=True),
    sa.Column('checkin', sa.Boolean(), nullable=True),
    sa.Column('triagem', sa.Boolean(), nullable=True),
    sa.Column('consulta', sa.Boolean(), nullable=True),
    sa.Column('checkout', sa.Boolean(), nullable=True),
    sa.Column('limpeza', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('agendamento'),
    sa.UniqueConstraint('cadastro'),
    sa.UniqueConstraint('checkin'),
    sa.UniqueConstraint('checkout'),
    sa.UniqueConstraint('consulta'),
    sa.UniqueConstraint('limpeza'),
    sa.UniqueConstraint('triagem')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('checklist')
    op.drop_table('agendamento')
    # ### end Alembic commands ###
