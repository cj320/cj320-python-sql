"""empty message

Revision ID: d04613ecc850
Revises: 84fa860bae3f
Create Date: 2021-12-22 19:22:34.656133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd04613ecc850'
down_revision = '84fa860bae3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contracts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('contract_name', sa.String(), nullable=False),
    sa.Column('customer_name', sa.String(), nullable=False),
    sa.Column('open_reqs', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contract_name')
    )
    op.create_table('labor_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('labor_code', sa.String(length=5), nullable=False),
    sa.Column('labor_category', sa.String(), nullable=False),
    sa.Column('salary', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email_address', sa.String(), nullable=False),
    sa.Column('labor_id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.ForeignKeyConstraint(['labor_id'], ['labor_categories.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address')
    )
    op.create_table('employees_to_contracts',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('employee_id', 'contract_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees_to_contracts')
    op.drop_table('employees')
    op.drop_table('labor_categories')
    op.drop_table('contracts')
    # ### end Alembic commands ###
