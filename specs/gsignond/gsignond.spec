%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$
%global dbus_type session


Name:           gsignond
Summary:        GSignOn daemon
Version:        1.0.6+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://gitlab.com/accounts-sso/%{name}
Source0:        %{name}-%{version}.tar.gz

# Patch to not build the Ostro OS and tizen extensions
Patch1:         00-disable-tizen-ostro.patch


BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  trousers-devel

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libecryptfs)
BuildRequires:  pkgconfig(sqlite3)

Requires:       %{name}-config

Requires:       dbus%{?_isa}


%description
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.


%package        libs
Summary:        GSignOn daemon libraries
%description    libs
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.

This package contains the shared libraries.


%package        devel
Summary:        GSignOn daemon development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.

This package contains the development headers.


%package        doc
Summary:        GSignOn daemon documentation
BuildArch:      noarch
%description    doc
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.

This package contains the documentation.


%package        default-config
Summary:        GSignOn daemon default configuration
BuildArch:      noarch
Provides:       %{name}-config
%description    default-config
The GSignOn daemon is a D-Bus service which performs user authentication
on behalf of its clients. There are currently authentication plugins for
OAuth 1.0 and 2.0, SASL, Digest-MD5, and plain username/password
combination.

This package contains the default configuration.


%prep
%autosetup -p1


%build
NOCONFIGURE=1 ./autogen.sh

%configure \
    --disable-static \
    --enable-dbus-type=%{dbus_type} \
    --enable-gtk-doc

%make_build


%install
%make_install

find %{buildroot} -name '*.la' -print -delete


%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig


%files
%{_bindir}/gsignond

%{_libdir}/gsignond/

%if %{dbus_type} != p2p
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOn.service
%endif


%files          libs
%license COPYING.LIB

%{_libdir}/libgsignond-common.so.0
%{_libdir}/libgsignond-common.so.0.0.0
%{_libdir}/girepository-1.0/gSignond-1.0.typelib


%files          devel
%{_includedir}/gsignond/

%{_libdir}/libgsignond-common.so
%{_libdir}/pkgconfig/gsignond.pc

%{_datadir}/dbus-1/interfaces/com.google.code.AccountsSSO.gSingleSignOn.*.xml
%{_datadir}/gir-1.0/gSignond-1.0.gir
%{_datadir}/vala/vapi/gsignond.deps
%{_datadir}/vala/vapi/gsignond.vapi


%files          doc
%{_datadir}/gtk-doc/html/gsignond/


%files          default-config
%config(noreplace) %{_sysconfdir}/gsignond.conf


%changelog
* Mon Oct 09 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git171009.185637.2d676c9b-1
- Update to latest snapshot.

* Sun Apr 23 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git170420.061410.38bbf6dd-1
- Initial package.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-2
- Fix subpackage descriptions.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Initial package.

