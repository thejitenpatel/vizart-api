"""removed product_image from products TB

Revision ID: 58c43aaf057d
Revises: 035a43aecf9a
Create Date: 2022-01-07 21:58:05.867038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58c43aaf057d'
down_revision = '035a43aecf9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'product_image')
    op.drop_column('product_category', 'deleted_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('product_image',
                  sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('product_category', sa.Column('deleted_at',
                  sa.VARCHAR(), autoincrement=False, nullable=False, default="now()"))
    # ### end Alembic commands ###