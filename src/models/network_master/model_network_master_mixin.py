from sqlalchemy.ext.declarative import declared_attr

from src import db
from src.drivers.enums.drivers import Drivers
from src.models.network_master.model_network_master import NetworkMasterModel


class NetworkMasterMixinModel(NetworkMasterModel):
    __abstract__ = True

    @classmethod
    def get_polymorphic_identity(cls) -> Drivers:
        pass

    @declared_attr
    def global_uuid(self):
        return db.Column(db.String(80), db.ForeignKey('networks_masters.global_uuid'), primary_key=True, nullable=False)

    @declared_attr
    def __mapper_args__(self):
        return {
            'polymorphic_identity': self.get_polymorphic_identity()
        }

    def __repr__(self):
        return f"{self.get_polymorphic_identity().value}NetworkMaster(global_uuid = {self.global_uuid})"
