%define rev 92
%define debug_package %{nil}

Summary: Switchboard System Settings Applications Plug
Name: switchboard-plug-applications
Version: 0.1.0.1~rev%{rev}
Release: 2%{?dist}
License: LGPLv3
URL: http://launchpad.net/switchboard-plug-applications

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Application Plug


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT

# This is quite broken
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-applications.desktop

%find_lang applications-plug


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f applications-plug.lang
%{_libdir}/switchboard/personal/pantheon-applications-plug
%{_datadir}/applications/pantheon-plug-applications.desktop
   

%changelog
* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev92-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev92-1
- Bump to version 0.1.0.1.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev88-1
- Update to new upstream snapshot.

* Mon Jul 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-1
- Initial package.


