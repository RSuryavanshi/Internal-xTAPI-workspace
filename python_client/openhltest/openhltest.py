from httptransport import HttpTransport
from yangbase import YangBase


class Openhltest(YangBase):
	"""This module is the top level of the test hierarchy. 
	"""
	def __init__(self, ip_address, rest_port):
		self.YANG_MODULE = ''
		self.YANG_CLASS = ''
		super(Openhltest, self).__init__(HttpTransport(ip_address, rest_port), None)

	def sessions(self, name=None):
		"""Get the sessions object(s) from the server.

		A list of test tool sessions.

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the sessions list.  

		Returns:  
			:obj:`list` of :obj:`Sessions` | :obj:`Sessions`: If arg name is None a list of Sessions objects otherwise a single Sessions object.  

		Raises:  
			NotFoundError: name is not in the list of sessions objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(Sessions(self, name))

	def create_sessions(self, name):
		"""Create a child sibling sessions instance on the server.

		A list of test tool sessions.

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`Sessions`: An object encapsulating an instance of the sessions model.  

		Raises:  
			AlreadyExistsError: An instance of sessions with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(Sessions(self, name), locals())


class Sessions(YangBase):
	"""A list of test tool sessions.
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'sessions'
		self.YANG_KEY = 'name'
		super(Sessions, self).__init__(parent, yang_key_value)

	def config(self):
		"""Get the config object from the server

		This container aggregates all other top level configuration submodules.

		Returns:  
			:obj:`SessionsConfig`: An object encapsulating an instance of the config model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfig(self))

	def statistics(self):
		"""Get the statistics object from the server

		The statistics pull model

		Returns:  
			:obj:`SessionsStatistics`: An object encapsulating an instance of the statistics model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsStatistics(self))

	def delete(self):
		"""Delete this sessions instance on the server.

		A list of test tool sessions.

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this sessions instance on the server with any changed property values.

		A list of test tool sessions.

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of the test tool session. Once the session has been created the name cannot be modified."""
		return self._get_value('name')

	@property
	def session_type(self):
		""":str:`enum`: The type of test tool session. Once the session has been created the session-type cannot be modified.  
		Enums:  
			L2L3: A layer 23 test tool session  
			L4L7: A layer 47 test tool session. This is currently not supported and is a feature placeholder  
		"""
		return self._get_value('session-type')

	@session_type.setter
	def session_type(self, value):
		return self._set_value('session-type', value)


class SessionsConfig(YangBase):
	"""This container aggregates all other top level configuration submodules.
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'config'
		super(SessionsConfig, self).__init__(parent, None)

	def ports(self, name=None):
		"""Get the ports object(s) from the server.

		A list of abstract test ports

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the ports list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigPorts` | :obj:`SessionsConfigPorts`: If arg name is None a list of SessionsConfigPorts objects otherwise a single SessionsConfigPorts object.  

		Raises:  
			NotFoundError: name is not in the list of ports objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigPorts(self, name))

	def create_ports(self, name):
		"""Create a child sibling ports instance on the server.

		A list of abstract test ports

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigPorts`: An object encapsulating an instance of the ports model.  

		Raises:  
			AlreadyExistsError: An instance of ports with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigPorts(self, name), locals())

	def config_ports(self):
		"""Get the config-ports object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigConfigPorts`: An object encapsulating an instance of the config-ports model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigConfigPorts(self))

	def device_groups(self, name=None):
		"""Get the device-groups object(s) from the server.

		A list of emulated device groups

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the device-groups list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigDeviceGroups` | :obj:`SessionsConfigDeviceGroups`: If arg name is None a list of SessionsConfigDeviceGroups objects otherwise a single SessionsConfigDeviceGroups object.  

		Raises:  
			NotFoundError: name is not in the list of device-groups objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroups(self, name))

	def create_device_groups(self, name):
		"""Create a child sibling device-groups instance on the server.

		A list of emulated device groups

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigDeviceGroups`: An object encapsulating an instance of the device-groups model.  

		Raises:  
			AlreadyExistsError: An instance of device-groups with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigDeviceGroups(self, name), locals())

	def traffic_groups(self, name=None):
		"""Get the traffic-groups object(s) from the server.

		A list of traffic groups

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the traffic-groups list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigTrafficGroups` | :obj:`SessionsConfigTrafficGroups`: If arg name is None a list of SessionsConfigTrafficGroups objects otherwise a single SessionsConfigTrafficGroups object.  

		Raises:  
			NotFoundError: name is not in the list of traffic-groups objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroups(self, name))

	def create_traffic_groups(self, name):
		"""Create a child sibling traffic-groups instance on the server.

		A list of traffic groups

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigTrafficGroups`: An object encapsulating an instance of the traffic-groups model.  

		Raises:  
			AlreadyExistsError: An instance of traffic-groups with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigTrafficGroups(self, name), locals())

	def delete(self):
		"""Delete this config instance on the server.

		This container aggregates all other top level configuration submodules.

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	class ConnectPortsInput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:input'
			self.port_map = []
			self.break_lock = ''

		class PortMap(object):
			"""TBD
			"""
			def __init__(self):
				self.port_name = ''
				self.chassis = ''
				self.card = ''
				self.port = ''

	class ConnectPortsOutput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:output'
			self.errata = []

		class Errata(object):
			"""A list of rpc errors. An empty list indicates no errors occurred
			"""
			def __init__(self):
				self.name = ''
				self.detail = ''
				self.stack_trace = ''

	def connect_ports(self, connect_ports_input):
		"""Execute the connect-ports action on the server

		Connect abstract test ports to physical hardware test ports and/or virtual machine test ports

		Args:  
			connect_ports_input (:obj:`ConnectPortsInput`):  An object encapsulating an instance of the connect-ports action input model.  

		Returns:  
			:obj:`ConnectPortsOutput`:  An object encapsulating an instance of the connect-ports action output model.  

		Raises:  
			BadRequestError: The connect_ports_input arg has invalid values.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/connect-ports', connect_ports_input)

	class DisconnectPortsInput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:input'
			self.port_names = []

	class DisconnectPortsOutput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:output'
			self.errata = []

		class Errata(object):
			"""A list of rpc errors. An empty list indicates no errors occurred
			"""
			def __init__(self):
				self.name = ''
				self.detail = ''
				self.stack_trace = ''

	def disconnect_ports(self, disconnect_ports_input):
		"""Execute the disconnect-ports action on the server

		Disconnect abstract test ports from any connected physical hardware test ports and/or virtual machine test ports

		Args:  
			disconnect_ports_input (:obj:`DisconnectPortsInput`):  An object encapsulating an instance of the disconnect-ports action input model.  

		Returns:  
			:obj:`DisconnectPortsOutput`:  An object encapsulating an instance of the disconnect-ports action output model.  

		Raises:  
			BadRequestError: The disconnect_ports_input arg has invalid values.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/disconnect-ports', disconnect_ports_input)

	class StartDevicesInput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:input'
			self.device_group_names = []

	class StartDevicesOutput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:output'
			self.errata = []

		class Errata(object):
			"""A list of rpc errors. An empty list indicates no errors occurred
			"""
			def __init__(self):
				self.name = ''
				self.detail = ''
				self.stack_trace = ''

	def start_devices(self, start_devices_input):
		"""Execute the start-devices action on the server

		Start one or more emulated device groups. An empty list signifies that all device groups will be started.

		Args:  
			start_devices_input (:obj:`StartDevicesInput`):  An object encapsulating an instance of the start-devices action input model.  

		Returns:  
			:obj:`StartDevicesOutput`:  An object encapsulating an instance of the start-devices action output model.  

		Raises:  
			BadRequestError: The start_devices_input arg has invalid values.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/start-devices', start_devices_input)

	class StopDevicesInput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:input'
			self.device_group_names = []

	class StopDevicesOutput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:output'
			self.errata = []

		class Errata(object):
			"""A list of rpc errors. An empty list indicates no errors occurred
			"""
			def __init__(self):
				self.name = ''
				self.detail = ''
				self.stack_trace = ''

	def stop_devices(self, stop_devices_input):
		"""Execute the stop-devices action on the server

		Stop one or more device groups. An empty list signifiels that all device groups will be stopped.

		Args:  
			stop_devices_input (:obj:`StopDevicesInput`):  An object encapsulating an instance of the stop-devices action input model.  

		Returns:  
			:obj:`StopDevicesOutput`:  An object encapsulating an instance of the stop-devices action output model.  

		Raises:  
			BadRequestError: The stop_devices_input arg has invalid values.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/stop-devices', stop_devices_input)

	class StartTrafficInput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:input'
			self.traffic_group_names = []

	class StartTrafficOutput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:output'
			self.errata = []

		class Errata(object):
			"""A list of rpc errors. An empty list indicates no errors occurred
			"""
			def __init__(self):
				self.name = ''
				self.detail = ''
				self.stack_trace = ''

	def start_traffic(self, start_traffic_input):
		"""Execute the start-traffic action on the server

		Start one or more traffic groups. An empty list signifies that all traffic groups will be started.

		Args:  
			start_traffic_input (:obj:`StartTrafficInput`):  An object encapsulating an instance of the start-traffic action input model.  

		Returns:  
			:obj:`StartTrafficOutput`:  An object encapsulating an instance of the start-traffic action output model.  

		Raises:  
			BadRequestError: The start_traffic_input arg has invalid values.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/start-traffic', start_traffic_input)

	class StopTrafficInput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:input'
			self.traffic_group_names = []

	class StopTrafficOutput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:output'
			self.errata = []

		class Errata(object):
			"""A list of rpc errors. An empty list indicates no errors occurred
			"""
			def __init__(self):
				self.name = ''
				self.detail = ''
				self.stack_trace = ''

	def stop_traffic(self, stop_traffic_input):
		"""Execute the stop-traffic action on the server

		Stop one or more traffic groups. An empty list signifies that all traffic groups will be stopped.

		Args:  
			stop_traffic_input (:obj:`StopTrafficInput`):  An object encapsulating an instance of the stop-traffic action input model.  

		Returns:  
			:obj:`StopTrafficOutput`:  An object encapsulating an instance of the stop-traffic action output model.  

		Raises:  
			BadRequestError: The stop_traffic_input arg has invalid values.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/stop-traffic', stop_traffic_input)

	def clear(self):
		"""Execute the clear action on the server

		Clear the current configuration

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/clear')

	class LoadInput(object):
		"""TBD
		"""
		def __init__(self):
			self.YANG_PATH = 'openhltest:input'
			self.vendor_config = ''

	def load(self, load_input):
		"""Execute the load action on the server

		Load a vendor specific configuration

		Args:  
			load_input (:obj:`LoadInput`):  An object encapsulating an instance of the load action input model.  

		Raises:  
			BadRequestError: The load_input arg has invalid values.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/load', load_input)


class SessionsConfigPorts(YangBase):
	"""A list of abstract test ports
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ports'
		self.YANG_KEY = 'name'
		super(SessionsConfigPorts, self).__init__(parent, yang_key_value)

	def delete(self):
		"""Delete this ports instance on the server.

		A list of abstract test ports

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ports instance on the server with any changed property values.

		A list of abstract test ports

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of an abstract test port"""
		return self._get_value('name')


class SessionsConfigConfigPorts(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'config-ports'
		super(SessionsConfigConfigPorts, self).__init__(parent, None)

	def port_map(self, port_name=None):
		"""Get the port-map object(s) from the server.

		TBD

		Args:  
			port_name (:obj:`str`, optional, default=None): A key value in the port-map list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigConfigPortsPortMap` | :obj:`SessionsConfigConfigPortsPortMap`: If arg port_name is None a list of SessionsConfigConfigPortsPortMap objects otherwise a single SessionsConfigConfigPortsPortMap object.  

		Raises:  
			NotFoundError: port_name is not in the list of port-map objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigConfigPortsPortMap(self, port_name))

	def create_port_map(self, port_name):
		"""Create a child sibling port-map instance on the server.

		TBD

		Args:  
			port_name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigConfigPortsPortMap`: An object encapsulating an instance of the port-map model.  

		Raises:  
			AlreadyExistsError: An instance of port-map with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigConfigPortsPortMap(self, port_name), locals())

	def aggregate_port(self, port_group_name=None):
		"""Get the aggregate-port object(s) from the server.

		TBD

		Args:  
			port_group_name (:obj:`str`, optional, default=None): A key value in the aggregate-port list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigConfigPortsAggregatePort` | :obj:`SessionsConfigConfigPortsAggregatePort`: If arg port_group_name is None a list of SessionsConfigConfigPortsAggregatePort objects otherwise a single SessionsConfigConfigPortsAggregatePort object.  

		Raises:  
			NotFoundError: port_group_name is not in the list of aggregate-port objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigConfigPortsAggregatePort(self, port_group_name))

	def create_aggregate_port(self, port_group_name):
		"""Create a child sibling aggregate-port instance on the server.

		TBD

		Args:  
			port_group_name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigConfigPortsAggregatePort`: An object encapsulating an instance of the aggregate-port model.  

		Raises:  
			AlreadyExistsError: An instance of aggregate-port with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigConfigPortsAggregatePort(self, port_group_name), locals())

	def delete(self):
		"""Delete this config-ports instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()


class SessionsConfigConfigPortsPortMap(YangBase):
	"""TBD
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'port-map'
		self.YANG_KEY = 'port_name'
		super(SessionsConfigConfigPortsPortMap, self).__init__(parent, yang_key_value)

	def delete(self):
		"""Delete this port-map instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this port-map instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def port_name(self):
		"""str: The name of an abstract test port"""
		return self._get_value('port_name')

	@property
	def speed(self):
		"""str: Maximum transfer Unit"""
		return self._get_value('speed')

	@speed.setter
	def speed(self, value):
		return self._set_value('speed', value)

	@property
	def media(self):
		"""str: Physical media"""
		return self._get_value('media')

	@media.setter
	def media(self, value):
		return self._set_value('media', value)


class SessionsConfigConfigPortsAggregatePort(YangBase):
	"""TBD
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'aggregate-port'
		self.YANG_KEY = 'port_group_name'
		super(SessionsConfigConfigPortsAggregatePort, self).__init__(parent, yang_key_value)

	def delete(self):
		"""Delete this aggregate-port instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this aggregate-port instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def port_group_name(self):
		"""str: Aggregate port name"""
		return self._get_value('port_group_name')

	@property
	def member_port_names(self):
		"""str: Physical media"""
		return self._get_value('member-port-names')

	@member_port_names.setter
	def member_port_names(self, value):
		return self._set_value('member-port-names', value)

	@property
	def transmit_algorithm(self):
		"""str: Physical media"""
		return self._get_value('transmit-algorithm')

	@transmit_algorithm.setter
	def transmit_algorithm(self, value):
		return self._set_value('transmit-algorithm', value)


class SessionsConfigDeviceGroups(YangBase):
	"""A list of emulated device groups
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'device-groups'
		self.YANG_KEY = 'name'
		super(SessionsConfigDeviceGroups, self).__init__(parent, yang_key_value)

	def devices(self, name=None):
		"""Get the devices object(s) from the server.

		A list of emulated device groups

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the devices list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigDeviceGroupsDevices` | :obj:`SessionsConfigDeviceGroupsDevices`: If arg name is None a list of SessionsConfigDeviceGroupsDevices objects otherwise a single SessionsConfigDeviceGroupsDevices object.  

		Raises:  
			NotFoundError: name is not in the list of devices objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevices(self, name))

	def create_devices(self, name):
		"""Create a child sibling devices instance on the server.

		A list of emulated device groups

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevices`: An object encapsulating an instance of the devices model.  

		Raises:  
			AlreadyExistsError: An instance of devices with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigDeviceGroupsDevices(self, name), locals())

	def delete(self):
		"""Delete this device-groups instance on the server.

		A list of emulated device groups

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this device-groups instance on the server with any changed property values.

		A list of emulated device groups

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of an emulated device group"""
		return self._get_value('name')

	@property
	def port_name(self):
		"""str: The list of port-names"""
		return self._get_value('port-name')

	@port_name.setter
	def port_name(self, value):
		return self._set_value('port-name', value)

	@property
	def devices_per_port(self):
		"""int32: The unique name of an emulated device group"""
		return self._get_value('devices-per-port')

	@devices_per_port.setter
	def devices_per_port(self, value):
		return self._set_value('devices-per-port', value)

	@property
	def device_group_link(self):
		"""str: The unique name of an emulated device group"""
		return self._get_value('device-group-link')

	@device_group_link.setter
	def device_group_link(self, value):
		return self._set_value('device-group-link', value)


class SessionsConfigDeviceGroupsDevices(YangBase):
	"""A list of emulated device groups
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'devices'
		self.YANG_KEY = 'name'
		super(SessionsConfigDeviceGroupsDevices, self).__init__(parent, yang_key_value)

	def ethernet(self, name=None):
		"""Get the ethernet object(s) from the server.

		A list of ethernet interface groups

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the ethernet list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigDeviceGroupsDevicesEthernet` | :obj:`SessionsConfigDeviceGroupsDevicesEthernet`: If arg name is None a list of SessionsConfigDeviceGroupsDevicesEthernet objects otherwise a single SessionsConfigDeviceGroupsDevicesEthernet object.  

		Raises:  
			NotFoundError: name is not in the list of ethernet objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesEthernet(self, name))

	def create_ethernet(self, name):
		"""Create a child sibling ethernet instance on the server.

		A list of ethernet interface groups

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesEthernet`: An object encapsulating an instance of the ethernet model.  

		Raises:  
			AlreadyExistsError: An instance of ethernet with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigDeviceGroupsDevicesEthernet(self, name), locals())

	def vlan(self, name=None):
		"""Get the vlan object(s) from the server.

		A list of vlan interface group

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the vlan list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigDeviceGroupsDevicesVlan` | :obj:`SessionsConfigDeviceGroupsDevicesVlan`: If arg name is None a list of SessionsConfigDeviceGroupsDevicesVlan objects otherwise a single SessionsConfigDeviceGroupsDevicesVlan object.  

		Raises:  
			NotFoundError: name is not in the list of vlan objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesVlan(self, name))

	def create_vlan(self, name):
		"""Create a child sibling vlan instance on the server.

		A list of vlan interface group

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesVlan`: An object encapsulating an instance of the vlan model.  

		Raises:  
			AlreadyExistsError: An instance of vlan with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigDeviceGroupsDevicesVlan(self, name), locals())

	def ipv4(self, name=None):
		"""Get the ipv4 object(s) from the server.

		A list of IPv4 interfaces

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the ipv4 list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigDeviceGroupsDevicesIpv4` | :obj:`SessionsConfigDeviceGroupsDevicesIpv4`: If arg name is None a list of SessionsConfigDeviceGroupsDevicesIpv4 objects otherwise a single SessionsConfigDeviceGroupsDevicesIpv4 object.  

		Raises:  
			NotFoundError: name is not in the list of ipv4 objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4(self, name))

	def create_ipv4(self, name):
		"""Create a child sibling ipv4 instance on the server.

		A list of IPv4 interfaces

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4`: An object encapsulating an instance of the ipv4 model.  

		Raises:  
			AlreadyExistsError: An instance of ipv4 with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigDeviceGroupsDevicesIpv4(self, name), locals())

	def bgp_config(self, name=None):
		"""Get the bgp-config object(s) from the server.

		A list of BGP device emualtion

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the bgp-config list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigDeviceGroupsDevicesBgpConfig` | :obj:`SessionsConfigDeviceGroupsDevicesBgpConfig`: If arg name is None a list of SessionsConfigDeviceGroupsDevicesBgpConfig objects otherwise a single SessionsConfigDeviceGroupsDevicesBgpConfig object.  

		Raises:  
			NotFoundError: name is not in the list of bgp-config objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfig(self, name))

	def create_bgp_config(self, name):
		"""Create a child sibling bgp-config instance on the server.

		A list of BGP device emualtion

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfig`: An object encapsulating an instance of the bgp-config model.  

		Raises:  
			AlreadyExistsError: An instance of bgp-config with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigDeviceGroupsDevicesBgpConfig(self, name), locals())

	def bgp_route_config(self, name=None):
		"""Get the bgp-route-config object(s) from the server.

		A list of BGP IPv4 routes

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the bgp-route-config list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfig` | :obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfig`: If arg name is None a list of SessionsConfigDeviceGroupsDevicesBgpRouteConfig objects otherwise a single SessionsConfigDeviceGroupsDevicesBgpRouteConfig object.  

		Raises:  
			NotFoundError: name is not in the list of bgp-route-config objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfig(self, name))

	def create_bgp_route_config(self, name):
		"""Create a child sibling bgp-route-config instance on the server.

		A list of BGP IPv4 routes

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfig`: An object encapsulating an instance of the bgp-route-config model.  

		Raises:  
			AlreadyExistsError: An instance of bgp-route-config with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigDeviceGroupsDevicesBgpRouteConfig(self, name), locals())

	def delete(self):
		"""Delete this devices instance on the server.

		A list of emulated device groups

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this devices instance on the server with any changed property values.

		A list of emulated device groups

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of an emulated device group"""
		return self._get_value('name')

	@property
	def device_count(self):
		"""int32: Number of emulated device group"""
		return self._get_value('device-count')

	@device_count.setter
	def device_count(self, value):
		return self._set_value('device-count', value)


class SessionsConfigDeviceGroupsDevicesEthernet(YangBase):
	"""A list of ethernet interface groups
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ethernet'
		self.YANG_KEY = 'name'
		super(SessionsConfigDeviceGroupsDevicesEthernet, self).__init__(parent, yang_key_value)

	def protocol_link(self):
		"""Get the protocol-link object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesEthernetProtocolLink`: An object encapsulating an instance of the protocol-link model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesEthernetProtocolLink(self))

	def mac_address(self):
		"""Get the mac_address object from the server

		MAC Address attribute

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesEthernetMac_address`: An object encapsulating an instance of the mac_address model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesEthernetMac_address(self))

	def delete(self):
		"""Delete this ethernet instance on the server.

		A list of ethernet interface groups

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ethernet instance on the server with any changed property values.

		A list of ethernet interface groups

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of an ethernet interface"""
		return self._get_value('name')


class SessionsConfigDeviceGroupsDevicesEthernetProtocolLink(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'protocol-link'
		super(SessionsConfigDeviceGroupsDevicesEthernetProtocolLink, self).__init__(parent, None)

	def delete(self):
		"""Delete this protocol-link instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this protocol-link instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def device_intf_link(self):
		"""str: Vertical Link"""
		return self._get_value('device-intf-link')

	@device_intf_link.setter
	def device_intf_link(self, value):
		return self._set_value('device-intf-link', value)

	@property
	def device_group_intf_link(self):
		"""str: Horizontal Link"""
		return self._get_value('device-group-intf-link')

	@device_group_intf_link.setter
	def device_group_intf_link(self, value):
		return self._set_value('device-group-intf-link', value)


class SessionsConfigDeviceGroupsDevicesEthernetMac_address(YangBase):
	"""MAC Address attribute
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'mac_address'
		super(SessionsConfigDeviceGroupsDevicesEthernetMac_address, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesEthernetMac_addressIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesEthernetMac_addressIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesEthernetMac_addressDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesEthernetMac_addressDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesEthernetMac_addressListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesEthernetMac_addressListPattern(self))

	def delete(self):
		"""Delete this mac_address instance on the server.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this mac_address instance on the server with any changed property values.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: Starting MAC Address value"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigDeviceGroupsDevicesEthernetMac_addressIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigDeviceGroupsDevicesEthernetMac_addressIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesEthernetMac_addressDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigDeviceGroupsDevicesEthernetMac_addressDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesEthernetMac_addressListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigDeviceGroupsDevicesEthernetMac_addressListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigDeviceGroupsDevicesVlan(YangBase):
	"""A list of vlan interface group
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'vlan'
		self.YANG_KEY = 'name'
		super(SessionsConfigDeviceGroupsDevicesVlan, self).__init__(parent, yang_key_value)

	def protocol_link(self):
		"""Get the protocol-link object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesVlanProtocolLink`: An object encapsulating an instance of the protocol-link model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesVlanProtocolLink(self))

	def delete(self):
		"""Delete this vlan instance on the server.

		A list of vlan interface group

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this vlan instance on the server with any changed property values.

		A list of vlan interface group

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of a vlan interface"""
		return self._get_value('name')

	@property
	def vlan_id(self):
		"""str: VLAN Identifier"""
		return self._get_value('vlan_id')

	@vlan_id.setter
	def vlan_id(self, value):
		return self._set_value('vlan_id', value)

	@property
	def priority(self):
		"""str: VLAN Priority"""
		return self._get_value('priority')

	@priority.setter
	def priority(self, value):
		return self._set_value('priority', value)

	@property
	def tpid(self):
		"""str: Tag Protocol Identifier"""
		return self._get_value('tpid')

	@tpid.setter
	def tpid(self, value):
		return self._set_value('tpid', value)


class SessionsConfigDeviceGroupsDevicesVlanProtocolLink(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'protocol-link'
		super(SessionsConfigDeviceGroupsDevicesVlanProtocolLink, self).__init__(parent, None)

	def delete(self):
		"""Delete this protocol-link instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this protocol-link instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def device_intf_link(self):
		"""str: Vertical Link"""
		return self._get_value('device-intf-link')

	@device_intf_link.setter
	def device_intf_link(self, value):
		return self._set_value('device-intf-link', value)

	@property
	def device_group_intf_link(self):
		"""str: Horizontal Link"""
		return self._get_value('device-group-intf-link')

	@device_group_intf_link.setter
	def device_group_intf_link(self, value):
		return self._set_value('device-group-intf-link', value)


class SessionsConfigDeviceGroupsDevicesIpv4(YangBase):
	"""A list of IPv4 interfaces
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ipv4'
		self.YANG_KEY = 'name'
		super(SessionsConfigDeviceGroupsDevicesIpv4, self).__init__(parent, yang_key_value)

	def protocol_link(self):
		"""Get the protocol-link object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4ProtocolLink`: An object encapsulating an instance of the protocol-link model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4ProtocolLink(self))

	def address(self):
		"""Get the address object from the server

		IPv4 Address

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4Address`: An object encapsulating an instance of the address model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4Address(self))

	def gateway(self):
		"""Get the gateway object from the server

		IPv4 Gateway

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4Gateway`: An object encapsulating an instance of the gateway model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4Gateway(self))

	def delete(self):
		"""Delete this ipv4 instance on the server.

		A list of IPv4 interfaces

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ipv4 instance on the server with any changed property values.

		A list of IPv4 interfaces

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of IPv4 interface"""
		return self._get_value('name')


class SessionsConfigDeviceGroupsDevicesIpv4ProtocolLink(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'protocol-link'
		super(SessionsConfigDeviceGroupsDevicesIpv4ProtocolLink, self).__init__(parent, None)

	def delete(self):
		"""Delete this protocol-link instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this protocol-link instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def device_intf_link(self):
		"""str: Vertical Link"""
		return self._get_value('device-intf-link')

	@device_intf_link.setter
	def device_intf_link(self, value):
		return self._set_value('device-intf-link', value)

	@property
	def device_group_intf_link(self):
		"""str: Horizontal Link"""
		return self._get_value('device-group-intf-link')

	@device_group_intf_link.setter
	def device_group_intf_link(self, value):
		return self._set_value('device-group-intf-link', value)


class SessionsConfigDeviceGroupsDevicesIpv4Address(YangBase):
	"""IPv4 Address
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'address'
		super(SessionsConfigDeviceGroupsDevicesIpv4Address, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4AddressIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4AddressIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4AddressDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4AddressDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4AddressListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4AddressListPattern(self))

	def delete(self):
		"""Delete this address instance on the server.

		IPv4 Address

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this address instance on the server with any changed property values.

		IPv4 Address

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: TBD"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigDeviceGroupsDevicesIpv4AddressIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigDeviceGroupsDevicesIpv4AddressIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesIpv4AddressDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigDeviceGroupsDevicesIpv4AddressDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesIpv4AddressListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigDeviceGroupsDevicesIpv4AddressListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigDeviceGroupsDevicesIpv4Gateway(YangBase):
	"""IPv4 Gateway
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'gateway'
		super(SessionsConfigDeviceGroupsDevicesIpv4Gateway, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4GatewayIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4GatewayIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4GatewayDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4GatewayDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesIpv4GatewayListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesIpv4GatewayListPattern(self))

	def delete(self):
		"""Delete this gateway instance on the server.

		IPv4 Gateway

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this gateway instance on the server with any changed property values.

		IPv4 Gateway

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: TBD"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigDeviceGroupsDevicesIpv4GatewayIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigDeviceGroupsDevicesIpv4GatewayIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesIpv4GatewayDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigDeviceGroupsDevicesIpv4GatewayDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesIpv4GatewayListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigDeviceGroupsDevicesIpv4GatewayListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigDeviceGroupsDevicesBgpConfig(YangBase):
	"""A list of BGP device emualtion
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'bgp-config'
		self.YANG_KEY = 'name'
		super(SessionsConfigDeviceGroupsDevicesBgpConfig, self).__init__(parent, yang_key_value)

	def protocol_link(self):
		"""Get the protocol-link object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigProtocolLink`: An object encapsulating an instance of the protocol-link model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigProtocolLink(self))

	def as_num(self):
		"""Get the as-num object from the server

		The Autonomous system number for the emulated BGP router

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigAsNum`: An object encapsulating an instance of the as-num model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigAsNum(self))

	def dut_as_num(self):
		"""Get the dut-as-num object from the server

		The Autonomous system number for the emulated BGP router

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNum`: An object encapsulating an instance of the dut-as-num model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNum(self))

	def delete(self):
		"""Delete this bgp-config instance on the server.

		A list of BGP device emualtion

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this bgp-config instance on the server with any changed property values.

		A list of BGP device emualtion

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of BGP device"""
		return self._get_value('name')

	@property
	def hold_time(self):
		"""str: The BGP Hold Time in seconds to use when negotiating with peers"""
		return self._get_value('hold-time')

	@hold_time.setter
	def hold_time(self, value):
		return self._set_value('hold-time', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigProtocolLink(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'protocol-link'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigProtocolLink, self).__init__(parent, None)

	def delete(self):
		"""Delete this protocol-link instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this protocol-link instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def device_intf_link(self):
		"""str: Vertical Link"""
		return self._get_value('device-intf-link')

	@device_intf_link.setter
	def device_intf_link(self, value):
		return self._set_value('device-intf-link', value)

	@property
	def device_group_intf_link(self):
		"""str: Horizontal Link"""
		return self._get_value('device-group-intf-link')

	@device_group_intf_link.setter
	def device_group_intf_link(self, value):
		return self._set_value('device-group-intf-link', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigAsNum(YangBase):
	"""The Autonomous system number for the emulated BGP router
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'as-num'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigAsNum, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigAsNumIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigAsNumIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigAsNumDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigAsNumDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigAsNumListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigAsNumListPattern(self))

	def delete(self):
		"""Delete this as-num instance on the server.

		The Autonomous system number for the emulated BGP router

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this as-num instance on the server with any changed property values.

		The Autonomous system number for the emulated BGP router

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: TBD"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigAsNumIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigAsNumIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigAsNumDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigAsNumDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigAsNumListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigAsNumListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNum(YangBase):
	"""The Autonomous system number for the emulated BGP router
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'dut-as-num'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNum, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumListPattern(self))

	def delete(self):
		"""Delete this dut-as-num instance on the server.

		The Autonomous system number for the emulated BGP router

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this dut-as-num instance on the server with any changed property values.

		The Autonomous system number for the emulated BGP router

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: TBD"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpConfigDutAsNumListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfig(YangBase):
	"""A list of BGP IPv4 routes
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'bgp-route-config'
		self.YANG_KEY = 'name'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfig, self).__init__(parent, yang_key_value)

	def protocol_link(self):
		"""Get the protocol-link object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigProtocolLink`: An object encapsulating an instance of the protocol-link model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigProtocolLink(self))

	def ipv4_network_group(self):
		"""Get the ipv4-network-group object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroup`: An object encapsulating an instance of the ipv4-network-group model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroup(self))

	def ipv6_network_group(self):
		"""Get the ipv6-network-group object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroup`: An object encapsulating an instance of the ipv6-network-group model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroup(self))

	def delete(self):
		"""Delete this bgp-route-config instance on the server.

		A list of BGP IPv4 routes

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this bgp-route-config instance on the server with any changed property values.

		A list of BGP IPv4 routes

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of an emulated BGP IPv4 route"""
		return self._get_value('name')

	@property
	def as_path(self):
		"""str: The AS Path of an emulated BGP IPv4 route"""
		return self._get_value('as_path')

	@as_path.setter
	def as_path(self, value):
		return self._set_value('as_path', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigProtocolLink(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'protocol-link'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigProtocolLink, self).__init__(parent, None)

	def delete(self):
		"""Delete this protocol-link instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this protocol-link instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def device_intf_link(self):
		"""str: Vertical Link"""
		return self._get_value('device-intf-link')

	@device_intf_link.setter
	def device_intf_link(self, value):
		return self._set_value('device-intf-link', value)

	@property
	def device_group_intf_link(self):
		"""str: Horizontal Link"""
		return self._get_value('device-group-intf-link')

	@device_group_intf_link.setter
	def device_group_intf_link(self, value):
		return self._set_value('device-group-intf-link', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroup(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ipv4-network-group'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroup, self).__init__(parent, None)

	def ipv4_address(self):
		"""Get the ipv4-address object from the server

		The IPv4 address of an emulated BGP IPv4 route

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4Address`: An object encapsulating an instance of the ipv4-address model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4Address(self))

	def delete(self):
		"""Delete this ipv4-network-group instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ipv4-network-group instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def network_count(self):
		"""int32: The Prefix Length of an emulated BGP IPv4 route"""
		return self._get_value('network-count')

	@network_count.setter
	def network_count(self, value):
		return self._set_value('network-count', value)

	@property
	def prefix_length(self):
		"""str: The Prefix Length of an emulated BGP IPv4 route"""
		return self._get_value('prefix-length')

	@prefix_length.setter
	def prefix_length(self, value):
		return self._set_value('prefix-length', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4Address(YangBase):
	"""The IPv4 address of an emulated BGP IPv4 route
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ipv4-address'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4Address, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressListPattern(self))

	def delete(self):
		"""Delete this ipv4-address instance on the server.

		The IPv4 address of an emulated BGP IPv4 route

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ipv4-address instance on the server with any changed property values.

		The IPv4 address of an emulated BGP IPv4 route

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: TBD"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv4NetworkGroupIpv4AddressListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroup(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ipv6-network-group'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroup, self).__init__(parent, None)

	def ipv6_address(self):
		"""Get the ipv6-address object from the server

		The IPv4 address of an emulated BGP IPv4 route

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6Address`: An object encapsulating an instance of the ipv6-address model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6Address(self))

	def delete(self):
		"""Delete this ipv6-network-group instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ipv6-network-group instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def network_count(self):
		"""int32: The Prefix Length of an emulated BGP IPv4 route"""
		return self._get_value('network-count')

	@network_count.setter
	def network_count(self, value):
		return self._set_value('network-count', value)

	@property
	def prefix_length(self):
		"""str: The Prefix Length of an emulated BGP IPv4 route"""
		return self._get_value('prefix-length')

	@prefix_length.setter
	def prefix_length(self, value):
		return self._set_value('prefix-length', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6Address(YangBase):
	"""The IPv4 address of an emulated BGP IPv4 route
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ipv6-address'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6Address, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressListPattern(self))

	def delete(self):
		"""Delete this ipv6-address instance on the server.

		The IPv4 address of an emulated BGP IPv4 route

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ipv6-address instance on the server with any changed property values.

		The IPv4 address of an emulated BGP IPv4 route

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: TBD"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigDeviceGroupsDevicesBgpRouteConfigIpv6NetworkGroupIpv6AddressListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigTrafficGroups(YangBase):
	"""A list of traffic groups
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'traffic-groups'
		self.YANG_KEY = 'name'
		super(SessionsConfigTrafficGroups, self).__init__(parent, yang_key_value)

	def frame_length(self):
		"""Get the frame-length object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameLength`: An object encapsulating an instance of the frame-length model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameLength(self))

	def frame_load(self):
		"""Get the frame-load object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameLoad`: An object encapsulating an instance of the frame-load model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameLoad(self))

	def frame(self, name=None):
		"""Get the frame object(s) from the server.

		A list frames

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the frame list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigTrafficGroupsFrame` | :obj:`SessionsConfigTrafficGroupsFrame`: If arg name is None a list of SessionsConfigTrafficGroupsFrame objects otherwise a single SessionsConfigTrafficGroupsFrame object.  

		Raises:  
			NotFoundError: name is not in the list of frame objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrame(self, name))

	def create_frame(self, name):
		"""Create a child sibling frame instance on the server.

		A list frames

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrame`: An object encapsulating an instance of the frame model.  

		Raises:  
			AlreadyExistsError: An instance of frame with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigTrafficGroupsFrame(self, name), locals())

	def delete(self):
		"""Delete this traffic-groups instance on the server.

		A list of traffic groups

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this traffic-groups instance on the server with any changed property values.

		A list of traffic groups

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name of a traffic group"""
		return self._get_value('name')

	@property
	def src_endpoint_device_group_names(self):
		"""str: The unique name of a traffic group"""
		return self._get_value('src-endpoint-device-group-names')

	@src_endpoint_device_group_names.setter
	def src_endpoint_device_group_names(self, value):
		return self._set_value('src-endpoint-device-group-names', value)

	@property
	def dest_endpoint_device_group_names(self):
		"""str: The unique name of a traffic group"""
		return self._get_value('dest-endpoint-device-group-names')

	@dest_endpoint_device_group_names.setter
	def dest_endpoint_device_group_names(self, value):
		return self._set_value('dest-endpoint-device-group-names', value)

	@property
	def protocol_interface(self):
		"""str: The unique name of a traffic group"""
		return self._get_value('protocol-interface')

	@protocol_interface.setter
	def protocol_interface(self, value):
		return self._set_value('protocol-interface', value)

	@property
	def bidirectional(self):
		"""bool: The unique name of a traffic group"""
		return self._get_value('bidirectional')

	@bidirectional.setter
	def bidirectional(self, value):
		return self._set_value('bidirectional', value)


class SessionsConfigTrafficGroupsFrameLength(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'frame-length'
		super(SessionsConfigTrafficGroupsFrameLength, self).__init__(parent, None)

	def fixed_mode(self):
		"""Get the fixed-mode object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameLengthFixedMode`: An object encapsulating an instance of the fixed-mode model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameLengthFixedMode(self))

	def delete(self):
		"""Delete this frame-length instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()


class SessionsConfigTrafficGroupsFrameLengthFixedMode(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'fixed-mode'
		super(SessionsConfigTrafficGroupsFrameLengthFixedMode, self).__init__(parent, None)

	def delete(self):
		"""Delete this fixed-mode instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this fixed-mode instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def frame_size(self):
		"""int32: The unique name of a traffic group"""
		return self._get_value('frame-size')

	@frame_size.setter
	def frame_size(self, value):
		return self._set_value('frame-size', value)


class SessionsConfigTrafficGroupsFrameLoad(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'frame-load'
		super(SessionsConfigTrafficGroupsFrameLoad, self).__init__(parent, None)

	def delete(self):
		"""Delete this frame-load instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this frame-load instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""int32: The unique name of a traffic group"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)

	@property
	def unit(self):
		"""str: The unique name of a traffic group"""
		return self._get_value('unit')

	@unit.setter
	def unit(self, value):
		return self._set_value('unit', value)


class SessionsConfigTrafficGroupsFrame(YangBase):
	"""A list frames
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'frame'
		self.YANG_KEY = 'name'
		super(SessionsConfigTrafficGroupsFrame, self).__init__(parent, yang_key_value)

	def ethernet_header(self, name=None):
		"""Get the ethernet-header object(s) from the server.

		A list frames

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the ethernet-header list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigTrafficGroupsFrameEthernetHeader` | :obj:`SessionsConfigTrafficGroupsFrameEthernetHeader`: If arg name is None a list of SessionsConfigTrafficGroupsFrameEthernetHeader objects otherwise a single SessionsConfigTrafficGroupsFrameEthernetHeader object.  

		Raises:  
			NotFoundError: name is not in the list of ethernet-header objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeader(self, name))

	def create_ethernet_header(self, name):
		"""Create a child sibling ethernet-header instance on the server.

		A list frames

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeader`: An object encapsulating an instance of the ethernet-header model.  

		Raises:  
			AlreadyExistsError: An instance of ethernet-header with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigTrafficGroupsFrameEthernetHeader(self, name), locals())

	def ipv4_header(self, name=None):
		"""Get the ipv4-header object(s) from the server.

		A list frames

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the ipv4-header list.  

		Returns:  
			:obj:`list` of :obj:`SessionsConfigTrafficGroupsFrameIpv4Header` | :obj:`SessionsConfigTrafficGroupsFrameIpv4Header`: If arg name is None a list of SessionsConfigTrafficGroupsFrameIpv4Header objects otherwise a single SessionsConfigTrafficGroupsFrameIpv4Header object.  

		Raises:  
			NotFoundError: name is not in the list of ipv4-header objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4Header(self, name))

	def create_ipv4_header(self, name):
		"""Create a child sibling ipv4-header instance on the server.

		A list frames

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4Header`: An object encapsulating an instance of the ipv4-header model.  

		Raises:  
			AlreadyExistsError: An instance of ipv4-header with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsConfigTrafficGroupsFrameIpv4Header(self, name), locals())

	def delete(self):
		"""Delete this frame instance on the server.

		A list frames

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this frame instance on the server with any changed property values.

		A list frames

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name"""
		return self._get_value('name')


class SessionsConfigTrafficGroupsFrameEthernetHeader(YangBase):
	"""A list frames
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ethernet-header'
		self.YANG_KEY = 'name'
		super(SessionsConfigTrafficGroupsFrameEthernetHeader, self).__init__(parent, yang_key_value)

	def src_mac(self):
		"""Get the src_mac object from the server

		MAC Address attribute

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_mac`: An object encapsulating an instance of the src_mac model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_mac(self))

	def dest_mac(self):
		"""Get the dest_mac object from the server

		MAC Address attribute

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeaderDest_mac`: An object encapsulating an instance of the dest_mac model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeaderDest_mac(self))

	def delete(self):
		"""Delete this ethernet-header instance on the server.

		A list frames

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ethernet-header instance on the server with any changed property values.

		A list frames

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name"""
		return self._get_value('name')

	@property
	def header_link(self):
		"""str: The unique name"""
		return self._get_value('header-link')

	@header_link.setter
	def header_link(self, value):
		return self._set_value('header-link', value)


class SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_mac(YangBase):
	"""MAC Address attribute
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'src_mac'
		super(SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_mac, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macListPattern(self))

	def delete(self):
		"""Delete this src_mac instance on the server.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this src_mac instance on the server with any changed property values.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: Starting MAC Address value"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigTrafficGroupsFrameEthernetHeaderSrc_macListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigTrafficGroupsFrameEthernetHeaderDest_mac(YangBase):
	"""MAC Address attribute
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'dest_mac'
		super(SessionsConfigTrafficGroupsFrameEthernetHeaderDest_mac, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macListPattern(self))

	def delete(self):
		"""Delete this dest_mac instance on the server.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this dest_mac instance on the server with any changed property values.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: Starting MAC Address value"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigTrafficGroupsFrameEthernetHeaderDest_macListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigTrafficGroupsFrameIpv4Header(YangBase):
	"""A list frames
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ipv4-header'
		self.YANG_KEY = 'name'
		super(SessionsConfigTrafficGroupsFrameIpv4Header, self).__init__(parent, yang_key_value)

	def src_address(self):
		"""Get the src_address object from the server

		MAC Address attribute

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_address`: An object encapsulating an instance of the src_address model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_address(self))

	def dest_address(self):
		"""Get the dest_address object from the server

		MAC Address attribute

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderDest_address`: An object encapsulating an instance of the dest_address model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderDest_address(self))

	def ttl(self):
		"""Get the ttl object from the server

		MAC Address attribute

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderTtl`: An object encapsulating an instance of the ttl model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderTtl(self))

	def delete(self):
		"""Delete this ipv4-header instance on the server.

		A list frames

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ipv4-header instance on the server with any changed property values.

		A list frames

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: The unique name"""
		return self._get_value('name')

	@property
	def header_link(self):
		"""str: The unique name"""
		return self._get_value('header-link')

	@header_link.setter
	def header_link(self, value):
		return self._set_value('header-link', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_address(YangBase):
	"""MAC Address attribute
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'src_address'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_address, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressListPattern(self))

	def delete(self):
		"""Delete this src_address instance on the server.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this src_address instance on the server with any changed property values.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: Starting MAC Address value"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderSrc_addressListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderDest_address(YangBase):
	"""MAC Address attribute
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'dest_address'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderDest_address, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressListPattern(self))

	def delete(self):
		"""Delete this dest_address instance on the server.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this dest_address instance on the server with any changed property values.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: Starting MAC Address value"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderDest_addressListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderTtl(YangBase):
	"""MAC Address attribute
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ttl'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderTtl, self).__init__(parent, None)

	def increment_pattern(self):
		"""Get the increment-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderTtlIncrementPattern`: An object encapsulating an instance of the increment-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderTtlIncrementPattern(self))

	def decrement_pattern(self):
		"""Get the decrement-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderTtlDecrementPattern`: An object encapsulating an instance of the decrement-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderTtlDecrementPattern(self))

	def list_pattern(self):
		"""Get the list-pattern object from the server

		TBD

		Returns:  
			:obj:`SessionsConfigTrafficGroupsFrameIpv4HeaderTtlListPattern`: An object encapsulating an instance of the list-pattern model.  

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsConfigTrafficGroupsFrameIpv4HeaderTtlListPattern(self))

	def delete(self):
		"""Delete this ttl instance on the server.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this ttl instance on the server with any changed property values.

		MAC Address attribute

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def value(self):
		"""str: Starting MAC Address value"""
		return self._get_value('value')

	@value.setter
	def value(self, value):
		return self._set_value('value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderTtlIncrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'increment-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderTtlIncrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this increment-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this increment-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderTtlDecrementPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'decrement-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderTtlDecrementPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this decrement-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this decrement-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def step_value(self):
		"""str: Step Value"""
		return self._get_value('step-value')

	@step_value.setter
	def step_value(self, value):
		return self._set_value('step-value', value)

	@property
	def count(self):
		"""str: Step Value"""
		return self._get_value('count')

	@count.setter
	def count(self, value):
		return self._set_value('count', value)

	@property
	def port_step_value(self):
		"""str: Port Step Value"""
		return self._get_value('port-step-value')

	@port_step_value.setter
	def port_step_value(self, value):
		return self._set_value('port-step-value', value)


class SessionsConfigTrafficGroupsFrameIpv4HeaderTtlListPattern(YangBase):
	"""TBD
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'list-pattern'
		super(SessionsConfigTrafficGroupsFrameIpv4HeaderTtlListPattern, self).__init__(parent, None)

	def delete(self):
		"""Delete this list-pattern instance on the server.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this list-pattern instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def list_value(self):
		"""str: Step Value"""
		return self._get_value('list-value')

	@list_value.setter
	def list_value(self, value):
		return self._set_value('list-value', value)


class SessionsStatistics(YangBase):
	"""The statistics pull model
	"""
	def __init__(self, parent):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'statistics'
		super(SessionsStatistics, self).__init__(parent, None)

	def ports(self, name=None):
		"""Get the ports object(s) from the server.

		TBD

		Args:  
			name (:obj:`str`, optional, default=None): A key value in the ports list.  

		Returns:  
			:obj:`list` of :obj:`SessionsStatisticsPorts` | :obj:`SessionsStatisticsPorts`: If arg name is None a list of SessionsStatisticsPorts objects otherwise a single SessionsStatisticsPorts object.  

		Raises:  
			NotFoundError: name is not in the list of ports objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsStatisticsPorts(self, name))

	def create_ports(self, name):
		"""Create a child sibling ports instance on the server.

		TBD

		Args:  
			name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsStatisticsPorts`: An object encapsulating an instance of the ports model.  

		Raises:  
			AlreadyExistsError: An instance of ports with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsStatisticsPorts(self, name), locals())

	def bgp_statistics(self, device_group_name=None):
		"""Get the bgp-statistics object(s) from the server.

		TBD

		Args:  
			device_group_name (:obj:`str`, optional, default=None): A key value in the bgp-statistics list.  

		Returns:  
			:obj:`list` of :obj:`SessionsStatisticsBgpStatistics` | :obj:`SessionsStatisticsBgpStatistics`: If arg device_group_name is None a list of SessionsStatisticsBgpStatistics objects otherwise a single SessionsStatisticsBgpStatistics object.  

		Raises:  
			NotFoundError: device_group_name is not in the list of bgp-statistics objects.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._read(SessionsStatisticsBgpStatistics(self, device_group_name))

	def create_bgp_statistics(self, device_group_name):
		"""Create a child sibling bgp-statistics instance on the server.

		TBD

		Args:  
			device_group_name (str): A unique key value that does not exist in the list on the server.  

		Returns:  
			:obj:`SessionsStatisticsBgpStatistics`: An object encapsulating an instance of the bgp-statistics model.  

		Raises:  
			AlreadyExistsError: An instance of bgp-statistics with the supplied key value already exists on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._create(SessionsStatisticsBgpStatistics(self, device_group_name), locals())

	def delete(self):
		"""Delete this statistics instance on the server.

		The statistics pull model

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._delete()

	def update(self):
		"""Update this statistics instance on the server with any changed property values.

		The statistics pull model

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def result_type(self):
		"""str: Timestamp of the first request to this session."""
		return self._get_value('result-type')

	@result_type.setter
	def result_type(self, value):
		return self._set_value('result-type', value)

	@property
	def port_name(self):
		"""str: The list of port-names"""
		return self._get_value('port-name')

	@port_name.setter
	def port_name(self, value):
		return self._set_value('port-name', value)

	@property
	def first_activity_timestamp(self):
		"""yang:date-and-time: Timestamp of the first request to this session."""
		return self._get_value('first-activity-timestamp')

	@property
	def last_activity_timestamp(self):
		"""yang:date-and-time: Timestamp of the last request to this session"""
		return self._get_value('last-activity-timestamp')

	def clear(self):
		"""Execute the clear action on the server

		Clear all statistic counters.

		Raises:  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._execute(self.url + '/clear')


class SessionsStatisticsPorts(YangBase):
	"""TBD
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ports'
		self.YANG_KEY = 'name'
		super(SessionsStatisticsPorts, self).__init__(parent, yang_key_value)

	def update(self):
		"""Update this ports instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: An abstract test port name"""
		return self._get_value('name')

	@property
	def connected_test_port_id(self):
		"""str: The id of the connected test port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('connected-test-port-id')

	@property
	def connected_test_port_description(self):
		"""str: Free form vendor specific description of the connected test port. Can include details such as make/model/productId of the underlying hardware. Empty if the abstract port is not connected to a test port."""
		return self._get_value('connected-test-port-description')

	@property
	def connection_state(self):
		""":str:`enum`: The state of the connection to the physical hardware test port or virtual machine test port  
		Enums:  
			CONNECTING: TBD  
			CONNECTED_LINK_UP: TBD  
			CONNECTED_LINK_DOWN: TBD  
			DISCONNECTING: TBD  
			DISCONNECTED: TBD  
		"""
		return self._get_value('connection-state')

	@property
	def connection_state_details(self):
		"""str: Free form vendor specific information about the state of the connection to the physical hardware test port or virtual machine test port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('connection-state-details')

	@property
	def speed(self):
		"""str: The actual speed of the test port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('speed')

	@property
	def tx_frames(self):
		"""str: The total number of frames transmitted on the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('tx-frames')

	@property
	def rx_frames(self):
		"""str: The total number of frames received on the the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('rx-frames')


class SessionsStatisticsBgpStatistics(YangBase):
	"""TBD
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'bgp-statistics'
		self.YANG_KEY = 'device_group_name'
		super(SessionsStatisticsBgpStatistics, self).__init__(parent, yang_key_value)

	def update(self):
		"""Update this bgp-statistics instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def port_name(self):
		"""str: An abstract test port name"""
		return self._get_value('port_name')

	@property
	def device_group_name(self):
		"""str: An abstract test port name"""
		return self._get_value('device_group_name')

	@property
	def router_state(self):
		""":str:`enum`: The state of the connection to the physical hardware test port or virtual machine test port  
		Enums:  
			IDLE: TBD  
			CONNECTING: TBD  
			ESTABLISHED: TBD  
		"""
		return self._get_value('router-state')

	@property
	def tx_advertise_route_count(self):
		"""str: The total number of frames transmitted on the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('tx-advertise-route-count')

	@property
	def rx_advertise_route_count(self):
		"""str: The total number of frames received on the the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('rx-advertise-route-count')

	@property
	def tx_withdraw_route_count(self):
		"""str: The total number of frames transmitted on the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('tx-withdraw-route-count')

	@property
	def rx_withdraw_route_count(self):
		"""str: The total number of frames received on the the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('rx-withdraw-route-count')


class SessionsStatisticEventsPorts(YangBase):
	"""TBD
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'ports'
		self.YANG_KEY = 'name'
		super(SessionsStatisticEventsPorts, self).__init__(parent, yang_key_value)

	def update(self):
		"""Update this ports instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def name(self):
		"""str: An abstract test port name"""
		return self._get_value('name')

	@property
	def connected_test_port_id(self):
		"""str: The id of the connected test port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('connected-test-port-id')

	@property
	def connected_test_port_description(self):
		"""str: Free form vendor specific description of the connected test port. Can include details such as make/model/productId of the underlying hardware. Empty if the abstract port is not connected to a test port."""
		return self._get_value('connected-test-port-description')

	@property
	def connection_state(self):
		""":str:`enum`: The state of the connection to the physical hardware test port or virtual machine test port  
		Enums:  
			CONNECTING: TBD  
			CONNECTED_LINK_UP: TBD  
			CONNECTED_LINK_DOWN: TBD  
			DISCONNECTING: TBD  
			DISCONNECTED: TBD  
		"""
		return self._get_value('connection-state')

	@property
	def connection_state_details(self):
		"""str: Free form vendor specific information about the state of the connection to the physical hardware test port or virtual machine test port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('connection-state-details')

	@property
	def speed(self):
		"""str: The actual speed of the test port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('speed')

	@property
	def tx_frames(self):
		"""str: The total number of frames transmitted on the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('tx-frames')

	@property
	def rx_frames(self):
		"""str: The total number of frames received on the the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('rx-frames')


class SessionsStatisticEventsBgpStatistics(YangBase):
	"""TBD
	"""
	def __init__(self, parent, yang_key_value=None):
		self.YANG_MODULE = 'openhltest'
		self.YANG_CLASS = 'bgp-statistics'
		self.YANG_KEY = 'device_group_name'
		super(SessionsStatisticEventsBgpStatistics, self).__init__(parent, yang_key_value)

	def update(self):
		"""Update this bgp-statistics instance on the server with any changed property values.

		TBD

		Raises:  
			NotFoundError: This instance does not exist on the server.  
			ServerError: An abnormal server error has occurred.  
		"""
		return self._update()

	@property
	def port_name(self):
		"""str: An abstract test port name"""
		return self._get_value('port_name')

	@property
	def device_group_name(self):
		"""str: An abstract test port name"""
		return self._get_value('device_group_name')

	@property
	def router_state(self):
		""":str:`enum`: The state of the connection to the physical hardware test port or virtual machine test port  
		Enums:  
			IDLE: TBD  
			CONNECTING: TBD  
			ESTABLISHED: TBD  
		"""
		return self._get_value('router-state')

	@property
	def tx_advertise_route_count(self):
		"""str: The total number of frames transmitted on the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('tx-advertise-route-count')

	@property
	def rx_advertise_route_count(self):
		"""str: The total number of frames received on the the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('rx-advertise-route-count')

	@property
	def tx_withdraw_route_count(self):
		"""str: The total number of frames transmitted on the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('tx-withdraw-route-count')

	@property
	def rx_withdraw_route_count(self):
		"""str: The total number of frames received on the the port. Empty if the abstract port is not connected to a test port."""
		return self._get_value('rx-withdraw-route-count')


