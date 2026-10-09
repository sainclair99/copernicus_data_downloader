# API DOC : https://documentation.dataspace.copernicus.eu/APIs/OData.html
collection : str = 'SENTINEL-2'
level : str = 'MSIL1C'
max_cloud_cover : float = 90.0
tile_id : str = '33PUK'
from_date : str = '2025-09-04T00:00:00.000Z'
to_date : str = '2026-07-28T23:59:59.999Z'

s2_full_filter =  (
    f"Collection/Name eq '{collection}' "
    f"and contains(Name, '{level}') "
    f"and ContentDate/Start ge '{from_date}' "
    f"and ContentDate/Start le '{to_date}' "
    "and Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' "
    f"and att/OData.CSC.DoubleAttribute/Value le {max_cloud_cover:.2f}) "
    "and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'tileId' "
    f"and att/OData.CSC.StringAttribute/Value eq '{tile_id}')"
),


# SENTINEL-1
collection2 : str = 'SENTINEL-1'
level2 : str = 'IW_GRDH_1S'
location_area : str = 'POLYGON((9.200 13.320,9.197 14.350,8.500 14.353,8.497 13.312,9.200 13.320))' # zone of interest

s1_full_filter =  (
    f"Collection/Name eq '{collection2}' "
    f"and contains(Name, '{level2}') "
    f"and not contains(Name, 'COG') "
    f"and ContentDate/Start ge '{from_date}' "
    f"and ContentDate/Start le '{to_date}' "
    f"and OData.CSC.Intersects(area=geography'SRID=4326;{location_area}')"
),
