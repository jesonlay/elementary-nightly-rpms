Summary:        elementary GTK+ Stylesheet
Name:           elementary-themes
Version:        5.0.1~git%{date}~%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://github.com/elementary/stylesheet

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch

Requires:       gtk-murrine-engine


%description
An original Gtk.CSS stylesheet designed specifically for elementary OS and its desktop environment: Pantheon.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_datadir}/themes/elementary

cp -p index.theme %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-2.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr gtk-3.0 %{buildroot}/%{_datadir}/themes/elementary/
cp -pr plank %{buildroot}/%{_datadir}/themes/elementary/


%clean
rm -rf %{buildroot}


%files
%doc AUTHORS CONTRIBUTORS HACKING
%license COPYING

%{_datadir}/themes/elementary


%changelog
* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160916.205458~8189f96b-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.1~git160911.211643~3457221a-1
- Update to version 5.0.1.


