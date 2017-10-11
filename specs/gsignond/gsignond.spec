%global __provides_exclude_from ^%{_libdir}/gsignond/.*\\.so$
%global dbus_type session
%global extension_type desktop

Name:           gsignond
Summary:        GSignOn daemon
Version:        1.0.6+git%{date}.%{commit}
Release:        2%{?dist}
License:        GPLv3

URL:            https://gitlab.com/accounts-sso/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  trousers-devel

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libecryptfs)
BuildRequires:  pkgconfig(libsecret-1)
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
%autosetup


%build
%meson -Dbus_type=%{dbus_type} -Dextension=%{extension_type}
%meson_build


%install
%meson_install


%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig


%files
%{_bindir}/gsignond

#%{_libdir}/gsignond/


%files          libs
%license COPYING.LIB

%{_libdir}/libgsignond-common.so.1
%{_libdir}/libgsignond-common.so.1.0.5

%{_libdir}/girepository-1.0/GSignond-1.0.typelib

%dir %{_libdir}/gsignond

%{_libdir}/gsignond/pluginloaders/

%dir %{_libdir}/gsignond/gplugins
%{_libdir}/gsignond/gplugins/libdigest.so
%{_libdir}/gsignond/gplugins/libpassword.so

%dir %{_libdir}/gsignond/extensions
%{_libdir}/gsignond/extensions/libextension-desktop.so


%files          devel
%{_includedir}/gsignond/

%{_libdir}/libgsignond-common.so
%{_libdir}/pkgconfig/gsignond.pc

%{_datadir}/gir-1.0/GSignond-1.0.gir
%{_datadir}/vala/vapi/gsignond.deps
%{_datadir}/vala/vapi/gsignond.vapi


%files          doc
%{_datadir}/gtk-doc/html/gsignond/


%files          default-config
%config(noreplace) %{_sysconfdir}/gsignond.conf


%changelog
* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git171011.073218.3d2b8a59-2
- Adapt to upstream changes.

* Wed Oct 11 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git171011.073218.3d2b8a59-1
- Update to latest snapshot.

* Tue Oct 10 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git171010.081348.5f0ba205-1
- Update to latest snapshot.

* Mon Oct 09 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git171009.190845.f917eead-1
- Update to latest snapshot.

* Mon Oct 09 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git171009.185637.2d676c9b-1
- Update to latest snapshot.

* Sun Apr 23 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6+git170420.061410.38bbf6dd-1
- Initial package.

* Tue Apr 18 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-2
- Fix subpackage descriptions.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Initial package.

