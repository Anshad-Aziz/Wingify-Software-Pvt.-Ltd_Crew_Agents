from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class AnalysisResult(Base):
    __tablename__ = 'analysis_results'
    id = Column(Integer, primary_key=True)
    query = Column(String)
    file_name = Column(String)
    analysis = Column(Text)
    task_id = Column(String)

engine = create_engine('sqlite:///results.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
