"""Second migration

Revision ID: b3acebf9c74c
Revises: 177213583f77
Create Date: 2024-11-13 12:32:04.638662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3acebf9c74c'
down_revision = '177213583f77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_onboardings_employee_id_employees'), 'employees', ['employee_id'], ['id'])

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_reviews_employee_id_employees'), 'employees', ['employee_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_reviews_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')

    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')

    # ### end Alembic commands ###
