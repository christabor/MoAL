import protobuff_pb2

package = protobuff_pb2.MoalPackage()
package.id = 0
package.pkg_name = "MoAL Package"
package.description = "An interesting package for learning things."
package.is_active = True
package.link = 'MOAL/MOAL/storage/serialization/protocol_buffers/protobuffs.py'

print(package)
