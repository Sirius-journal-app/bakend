"""initial

Revision ID: f30afae0c652
Revises: 
Create Date: 2024-03-23 18:25:59.674319

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'f30afae0c652'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classrooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('qualification', sa.String(), nullable=False),
    sa.Column('education', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('surname', sa.String(length=64), nullable=False),
    sa.Column('date_of_birth', sa.DateTime(timezone=True), nullable=True),
    sa.Column('profile_photo_uri', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('hashed_password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('competencies',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('teacher_id', 'subject_id')
    )
    op.create_table('students',
    sa.Column('admission_year', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('surname', sa.String(length=64), nullable=False),
    sa.Column('date_of_birth', sa.DateTime(timezone=True), nullable=True),
    sa.Column('profile_photo_uri', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('hashed_password', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('starts_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('duration', sa.Interval(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('classroom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classroom_id'], ['classrooms.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['teacher_id', 'subject_id'], ['competencies.teacher_id', 'competencies.subject_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('academic_reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=True),
    sa.Column('is_attended', sa.Boolean(), nullable=False),
    sa.Column('grade', sa.Enum('TERRIBLY', 'AWFULLY', 'UNSATISFACTORILY', 'SATISFACTORILY', 'GOOD', 'EXCELLENT', name='graduation'), nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['classes.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('academic_reports')
    op.drop_table('classes')
    op.drop_table('students')
    op.drop_table('competencies')
    op.drop_table('teachers')
    op.drop_table('subjects')
    op.drop_table('groups')
    op.drop_table('classrooms')
    # ### end Alembic commands ###