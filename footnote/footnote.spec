%define rev 339

Summary: A beautiful, fast, and simple note taking app in the style of elementary
Name: footnote
Version: 0.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/footnote

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala vala-tools gettext

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(sqlheavy-0.1)
# This does not work


%description
An very light and neat Notebook App for elementary OS.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post

%postun


%files



%changelog

