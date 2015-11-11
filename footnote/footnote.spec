%define rev 360

Summary: Beautiful, fast, and simple note taking app in the style of elementary
Name: footnote
Version: 0.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/footnote

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.11.6
#BuildRequires: pkgconfig(sqlheavy-0.1)


%description
Beautiful, fast, and simple note taking app in the style of elementary


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
# %%find_lang pantheon-datetime-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-datetime.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files
# -f pantheon-datetime-plug.lang
#%%{_libdir}/switchboard/system/pantheon-datetime
#%%{_datadir}/applications/pantheon-plug-datetime.desktop


%changelog


