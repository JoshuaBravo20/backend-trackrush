"""empty message

Revision ID: 85ccd81cfd6e
Revises: d0eee653bd4b
Create Date: 2021-02-19 22:59:30.670088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '85ccd81cfd6e'
down_revision = 'd0eee653bd4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.String(length=120), nullable=False))
    op.drop_constraint('posts_ibfk_1', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'user', ['user_id'], ['user_id'], ondelete='CASCADE')
    op.drop_column('posts', 'users_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('users_id', mysql.VARCHAR(length=120), nullable=False))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_ibfk_1', 'posts', 'user', ['users_id'], ['user_id'], ondelete='CASCADE')
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###
