# Copyright 2020, OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from opentelemetry.instrumentation.aiohttp_client.package import _instruments
from opentelemetry.instrumentation.aiohttp_client.client import AioHttpClientInstrumentor
from opentelemetry.instrumentation.aiohttp_client.server import AioHttpServerInstrumentor
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor

from typing import Collection


class AioHttpInstrumentor(BaseInstrumentor):
    """An instrumentor for aiohttp client sessions

    See `BaseInstrumentor`
    """

    def instrumentation_dependencies(self) -> Collection[str]:
        return _instruments

    def _instrument(self, **kwargs):
        """Instruments aiohttp ClientSession

        Args:
            **kwargs: Optional arguments
                ``tracer_provider``: a TracerProvider, defaults to global
                ``url_filter``: A callback to process the requested URL prior to adding
                    it as a span attribute. This can be useful to remove sensitive data
                    such as API keys or user personal information.
                ``request_hook``: An optional callback that is invoked right after a span is created.
                ``response_hook``: An optional callback which is invoked right before the span is finished processing a response.
        """
        AioHttpClientInstrumentor._instrument(
            tracer_provider=kwargs.get("tracer_provider"),
            url_filter=kwargs.get("url_filter"),
            request_hook=kwargs.get("request_hook"),
            response_hook=kwargs.get("response_hook"),
        )
        AioHttpServerInstrumentor._instrument(
            tracer_provider=kwargs.get("tracer_provider"),
            url_filter=kwargs.get("url_filter"),
            request_hook=kwargs.get("request_hook"),
            response_hook=kwargs.get("response_hook"),
        )

    def _uninstrument(self, **kwargs):
        AioHttpClientInstrumentor._uninstrument()
        AioHttpServerInstrumentor._uninstrument()
