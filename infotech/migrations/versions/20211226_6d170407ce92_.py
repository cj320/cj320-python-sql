"""empty message

Revision ID: 6d170407ce92
Revises: 91fde1ed2b8b
Create Date: 2021-12-26 16:08:45.822425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d170407ce92'
down_revision = '91fde1ed2b8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee_to_contracts',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.Column('labor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['labor_id'], ['labor_categories.id'], ),
    sa.PrimaryKeyConstraint('employee_id', 'contract_id', 'labor_id')
    )
    op.drop_table('employee_associations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee_associations',
    sa.Column('employee_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('contract_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('labor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], name='employee_associations_contract_id_fkey'),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name='employee_associations_employee_id_fkey'),
    sa.ForeignKeyConstraint(['labor_id'], ['labor_categories.id'], name='employee_associations_labor_id_fkey'),
    sa.PrimaryKeyConstraint('employee_id', 'contract_id', 'labor_id', name='employee_associations_pkey')
    )
    op.drop_table('employee_to_contracts')
    # ### end Alembic commands ###
