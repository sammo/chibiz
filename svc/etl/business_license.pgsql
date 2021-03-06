DROP TABLE IF EXISTS business_license;

CREATE TABLE IF NOT EXISTS business_license(
	id 									varchar,
	license_id							integer,
	account_number						integer,
	site_number							integer,
	legal_name							varchar,
	doing_business_as_name				varchar,
	address								varchar,
	city								varchar,
	state								varchar,
	zip_code							varchar,
	ward								integer,
	precinct							integer,
	ward_precinct						varchar,
	police_district						integer,
	license_code						integer,
	license_description					varchar,
	business_activity_id				varchar,
	business_activity					varchar,
	license_number						integer,
	application_type					varchar,
	application_created_date			timestamp,
	application_requirements_complete	timestamp,
	payment_date						timestamp,
	conditional_approval				varchar,
	license_start_date					timestamp,
	expiration_date						timestamp,
	license_approved_for_issuance		timestamp,
	date_issued							timestamp,
	license_status						varchar,
	license_status_change_date			timestamp,
	ssa									varchar,
	latitude							float,
	longitude							float,
	business_location					varchar,
	lastupdated							timestamp 		CONSTRAINT df_business_license_lastupdate DEFAULT now()
);
