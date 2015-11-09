%define rev 489

Summary: Gala window manager
Name: gala
Version: 0.2.0~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/gala

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: libtool pkgconfig
BuildRequires: vala vala-tools gettext
BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libbamf3)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libmutter)
BuildRequires: pkgconfig(plank)


%description
Gala is Pantheon's Window Manager, part of the elementary project.


%package devel
Summary: Gala window manager
%description devel
Gala is Pantheon's Window Manager, part of the elementary project. This package contains the development headers.


%prep
%setup -q


%build
./autogen.sh

%configure


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%{_libdir}/*.la
rm $RPM_BUILD_ROOT/%{_libdir}/gala/plugins/*.la

desktop-file-install data/gala.desktop							\
	--dir=$RPM_BUILD_ROOT/%{_datadir}/applications				\
	--set-key='Categories' --set-value='GNOME;GTK;'

mv data/gala-multitaskingview.desktop.in data/gala-multitaskingview.desktop

desktop-file-install data/gala-multitaskingview.desktop			\
	--dir=$RPM_BUILD_ROOT/%{_datadir}/applications 				\
	--set-key='Categories' --set-value='GNOME;GTK;'				\
	--set-key='Name' --set-value='Multitasking View'			\
	--set-key='Comment'											\
	--set-value='Comment=View all open windows and workspaces'	\
	--remove-key='_Name' --remove-key='_Comment'

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/gala-wayland.desktop

%find_lang gala


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null
 
%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f gala.lang
%{_bindir}/gala
%{_libdir}/gala/

%{_libdir}/libgala.so.0
%{_libdir}/libgala.so.0.0.0

%{_datadir}/gala/

%{_datadir}/applications/gala.desktop
%{_datadir}/applications/gala-multitaskingview.desktop
%{_datadir}/applications/gala-wayland.desktop

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml

%{_datadir}/icons/hicolor/32x32/apps/multitasking-view.svg
%{_datadir}/icons/hicolor/48x48/apps/multitasking-view.svg
%{_datadir}/icons/hicolor/64x64/apps/multitasking-view.svg


%files devel
%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc

%{_includedir}/gala
%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi


%changelog
* Sun Nov 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev489-1
- Update to new upstream snapshot.

* Sat Nov 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev488-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev485-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev484-1
- Update to new upstream snapshot.

* Sun Sep 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev483-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev482-1
- Update to new upstream snapshot.

* Fri Sep 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev479-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev476-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev475-2
- rebuild trigger for granite soname bump

* Thu Jul 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev475-1
- Update to bzr snapshot revno 475.

* Sun Jul 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev474-1
- Clean up spec file. Update to new bzr snapshot. Add -devel subpkg.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0~rev441-4
- Update to latest bzr snapshot.

* Sun Feb 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0~rev431-3
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1.0~rev429-2
- Fix upstream version.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev427-1
- Initial package.
