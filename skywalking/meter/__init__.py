#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from skywalking import config

_meter_service = None


def init():
    from skywalking.meter.meter_service import MeterService

    global _meter_service
    if _meter_service:
        return

    _meter_service = MeterService()
    _meter_service.start()

    if config.pvm_meter_reporter_active:
        from skywalking.meter.pvm.cpu_usage import CPUUsageDataSource
        from skywalking.meter.pvm.gc_data import GCDataSource
        from skywalking.meter.pvm.mem_usage import MEMUsageDataSource
        from skywalking.meter.pvm.thread_data import ThreadDataSource

        MEMUsageDataSource().registry()
        CPUUsageDataSource().registry()
        GCDataSource().registry()
        ThreadDataSource().registry()