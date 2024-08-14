def migrate(cr, version=None):
    cr.execute(
        """
        insert into fleet_vehicle_driver (vehicle_id, driver_id, date_start)
        select id, driver_id, create_date from fleet_vehicle where driver_id is not null
        """
    )
