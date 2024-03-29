"""added unique key to all FK

Revision ID: f6d0c2c43160
Revises: 9d8bf62d8635
Create Date: 2022-01-04 12:38:49.007656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6d0c2c43160'
down_revision = '9d8bf62d8635'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cart', ['category_id'])
    op.create_unique_constraint(None, 'cart', ['product_id'])
    op.create_unique_constraint(None, 'cart', ['inventory_id'])
    op.create_unique_constraint(None, 'cart', ['user_id'])
    op.create_unique_constraint(None, 'order_details', ['payment_id'])
    op.create_unique_constraint(None, 'order_details', ['user_id'])
    op.create_unique_constraint(None, 'order_items', ['product_id'])
    op.create_unique_constraint(None, 'order_items', ['category_id'])
    op.create_unique_constraint(None, 'order_items', ['order_id'])
    op.create_unique_constraint(None, 'order_items', ['user_id'])
    op.create_unique_constraint(None, 'order_items', ['payment_id'])
    op.create_unique_constraint(None, 'order_items', ['inventory_id'])
    op.create_unique_constraint(None, 'otp', ['user_id'])
    op.create_unique_constraint(None, 'product_image', ['inventory_id'])
    op.create_unique_constraint(None, 'product_image', ['product_id'])
    op.create_unique_constraint(None, 'product_image', ['category_id'])
    op.create_unique_constraint(None, 'tokens', ['user_id'])
    op.create_unique_constraint(None, 'upload_image', ['user_id'])
    op.create_unique_constraint(None, 'user_address', ['user_id'])
    op.create_unique_constraint(None, 'user_payments', ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_payments', type_='unique')
    op.drop_constraint(None, 'user_address', type_='unique')
    op.drop_constraint(None, 'upload_image', type_='unique')
    op.drop_constraint(None, 'tokens', type_='unique')
    op.drop_constraint(None, 'product_image', type_='unique')
    op.drop_constraint(None, 'product_image', type_='unique')
    op.drop_constraint(None, 'product_image', type_='unique')
    op.drop_constraint(None, 'otp', type_='unique')
    op.drop_constraint(None, 'order_items', type_='unique')
    op.drop_constraint(None, 'order_items', type_='unique')
    op.drop_constraint(None, 'order_items', type_='unique')
    op.drop_constraint(None, 'order_items', type_='unique')
    op.drop_constraint(None, 'order_items', type_='unique')
    op.drop_constraint(None, 'order_items', type_='unique')
    op.drop_constraint(None, 'order_details', type_='unique')
    op.drop_constraint(None, 'order_details', type_='unique')
    op.drop_constraint(None, 'cart', type_='unique')
    op.drop_constraint(None, 'cart', type_='unique')
    op.drop_constraint(None, 'cart', type_='unique')
    op.drop_constraint(None, 'cart', type_='unique')
    # ### end Alembic commands ###
