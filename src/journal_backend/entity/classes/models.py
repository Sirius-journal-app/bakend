from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Optional

from sqlalchemy import DateTime, ForeignKey, ForeignKeyConstraint, Interval
from sqlalchemy.orm import Mapped, mapped_column, relationship

from journal_backend.database.base import Base
from journal_backend.entity.academic_reports.models import AcademicReport

if TYPE_CHECKING:
    from journal_backend.entity.students.models import Group
    from journal_backend.entity.teachers.models import Subject, Teacher

DEFAULT_CLASS_DURATION = timedelta(minutes=60 * 1.5)


class Class(Base):  # type: ignore[misc]
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(primary_key=True)
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    duration: Mapped[timedelta] = mapped_column(
        Interval(native=True),
        default=DEFAULT_CLASS_DURATION
    )
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    teacher_id: Mapped[Optional[int]] = mapped_column(ForeignKey("teachers.id"))
    subject_id: Mapped[Optional[int]] = mapped_column(ForeignKey("subjects.id"))
    classroom_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("classrooms.id", ondelete="SET NULL")
    )

    academic_reports: Mapped[list["AcademicReport"]] = relationship(back_populates="lesson")
    group: Mapped["Group"] = relationship(back_populates="classes",)
    teacher: Mapped["Teacher"] = relationship(back_populates="classes")
    subject: Mapped["Subject"] = relationship(back_populates="classes")
    classroom: Mapped["Classroom"] = relationship(back_populates="classes")

    __table_args__ = (
        ForeignKeyConstraint(
            [teacher_id, subject_id],
            ["competencies.teacher_id", "competencies.subject_id"]
        ),
    )


class Classroom(Base):  # type: ignore[misc]
    __tablename__ = "classrooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    classes: Mapped[list["Class"]] = relationship(back_populates="classroom")
