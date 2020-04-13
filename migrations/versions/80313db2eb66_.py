"""empty message

Revision ID: 80313db2eb66
Revises: 6ee0b5ce0bdd
Create Date: 2020-03-12 14:02:20.146340

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '80313db2eb66'
down_revision = '6ee0b5ce0bdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('time_created', sa.String(length=255), nullable=True))
    op.drop_column('profiles', 'created')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('profiles', 'time_created')
    # ### end Alembic commands ###
