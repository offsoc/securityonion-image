# Copyright Security Onion Solutions, LLC

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

FROM ghcr.io/security-onion-solutions/oraclelinux:9

LABEL maintainer="Security Onion Solutions, LLC"
LABEL description="Replay PCAPs to sniffing interface(s)"

# Common Oracle layer
RUN dnf update -y && dnf -y install epel-release bash libpcap iproute && \
    dnf clean all && rm -rf /var/cache/dnf/* 

# Packages Specific to this Container
RUN dnf config-manager --enable ol9_codeready_builder && dnf -y install oraclelinux-developer-release-el9 && dnf repolist && \ 
    dnf -y install rpmrebuild alien wget libnsl && \
    dnf -y erase epel-release && dnf clean all && rm -rf /var/cache/dnf/* 


# Copy over tcpreplay - using v4.2.6 instead of 4.3.x because of known bugs: https://github.com/appneta/tcpreplay/issues/557
COPY files/tcpreplay /usr/local/bin/tcpreplay

# User configuration

RUN for i in securityonion-samples_20121202-0ubuntu0securityonion4_all.deb securityonion-samples-bro_20170824-1ubuntu1securityonion3_all.deb securityonion-samples-markofu_20130522-0ubuntu0securityonion3_all.deb securityonion-samples-mta_20190514-1ubuntu1securityonion1_all.deb securityonion-samples-shellshock_20140926-0ubuntu0securityonion2_all.deb; do wget https://launchpad.net/~securityonion/+archive/ubuntu/stable/+files/$i; done && \
\ 
alien -r *.deb && \
\
for i in securityonion-samples-20121202-1.noarch.rpm securityonion-samples-bro-20170824-2.noarch.rpm securityonion-samples-markofu-20130522-1.noarch.rpm securityonion-samples-mta-20190514-2.noarch.rpm securityonion-samples-shellshock-20140926-1.noarch.rpm  ; do rpmrebuild -p --change-spec-files='sed -e "s/%dir.*\"\/\"/#/"' -d/tmp/ $i && rpm -ivh /tmp/noarch/$i; done && \
\
rm *.deb && \
rm *.rpm

ENTRYPOINT ["/bin/bash"]
